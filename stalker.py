from requests import Session
import json
players_cache = {}
version = None
class Player(object):
    def __init__(self, id, name, profileIconId, summonerLevel, revisionDate):
        self.id = id
        self.name = name
        self.profileIconId = profileIconId
        self.summonerLevel = summonerLevel
        self.revisionDate = revisionDate
    def __str__(self):
        return "<"+str(self.name) + " " + str(self.id)+">"
    def __repr__(self):
        return self.__str__()

class Settings(object):
    MIN_INTERVAL = 30000
    def __init__(self, interval=600000, targets=[]):
        self.interval = interval if interval >= Settings.MIN_INTERVAL else Settings.MIN_INTERVAL
        self.targets = targets
    def __str__(self):
        return "< Settings:"+str(self.targets) + " (" + str(self.interval)+")>"
    def __repr__(self):
        return self.__str__()
def get(url, callback):
    with Session() as session:
        session.get(url, hooks=dict(response=callback))

def player_info(key, names, callback):
    names = map(lambda name: name.lower(), names)
    remaining = filter(lambda name: name not in players_cache.keys(), names)
    def to_Player(response, *args, **kwargs):
        if response.status_code == 200:
            try:
                obj = json.loads(response.text)
            except:
                obj = {}
            callback([ Player(**v) for (k,v) in obj.items()] + [players_cache[name] for name in filter(lambda n: n not in remaining, names)])
        elif response.status_code == 429:
            raise Exception('API rate limit has been reached. Please wait a while before attempting again')
        else:
            callback([players_cache[name] for name in filter(lambda n: n not in remaining, names)])
    if remaining:
        get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+",".join(remaining)+"?api_key="+key, to_Player)
    else:
        to_Player(None)
        
def lol_version(key, callback):
    def got_version(response, *args, **kwargs):
        obj = json.loads(response.text)
        version = obj[0]
        callback(version)
    if not version:
        get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key="+key, got_version)
    else:
        callback(version)
        
def summoner_icons(key, names, callback):
    lol_version(key, lambda version: player_info(key, names, lambda players: callback(map(lambda player: "http://ddragon.leagueoflegends.com/cdn/"+str(version)+"/img/profileicon/"+str(player.profileIconId)+".png", players)) ))

def current_game(key, names, callback):
    current_games = {}
    def get_id(players):
        for player in players:
            def got_current_game(response, *args, **kwargs):
                if response.status_code == 200 :
                    obj = json.loads(response.text)
                    current_games[player] = obj['gameId']
                else:
                    current_games[player] = None
                if len(current_games) == len(players):
                    callback( current_games )
            get("https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/"+str(player.id)+"?api_key="+key, got_current_game)
    player_info(key, names, get_id)
    
def record(gameId, callback):
    def try_record(response, *args, **kwargs):
        obj = json.loads(response.text)
        try :
            if obj.success:
                print('now recording game: '+str(gameId))
                callback(True)
            else:
                callback(False)
        except:
            callback(False)
    get("http://na.op.gg/summoner/ajax/requestRecording.json/gameId="+str(gameId), try_record)
    
def scan(key, names, callback):
    games = {}
    def playing( status_map):
        gameIds = [ v  for (k,v) in status_map.items() if v]
        if gameIds :
            for gameId in gameIds:
                def recording_callback(message):
                    games[gameId] = True if message else False
                    if len(games) == len(gameIds):
                        callback(games)
                record(gameId, recording_callback)
        else:
            callback(games)
    current_game(key, names, playing)
    
if __name__=='__main__':
    import time
    import argparse

    parser = argparse.ArgumentParser(description='League watcher')
    parser.add_argument('developer_key', help='Get your developer key at https://developer.riotgames.com/, by logging in to your account. This will be used to call lol server.')
    parser.add_argument('summoners', type=str, nargs='*', help='summoners you with to record videos for')
    parser.add_argument('-interval', '-i', type=int, help='The time (in ms) between each ping to lol server. Minimum value is 30000 and default is 600000 ms.')
    parser.add_argument('-settings', '-s', default='./settings.txt', type=str, help='Change the location of the settings file')
    args = parser.parse_args()

    def output(response, *args, **kwargs):
        print (response)
    MIN_INTERVAL = 30000
    summoners = []
    interval = 0
    with open(args.settings, 'r') as config:
            lines = "".join(config.readlines())
            obj = json.loads('{'+lines+'}')
            s = Settings(**obj)
            summoners = s.targets
            interval = s.interval if s.interval >= MIN_INTERVAL else MIN_INTERVAL
    if args.interval:
        interval = args.interval if args.interval >= MIN_INTERVAL else MIN_INTERVAL
    if args.summoners:
        summoners = args.summoners
    while True:
        scan(key, summoners, output)
        time.sleep(interval)

