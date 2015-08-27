# SummonerStalker
Puts a big brother on a set of summoners, recording them whenever they are in a game.

Description:
A console program running on python that will poll riot api server for current games of several summoners. If they are inside a game the program will contact op.gg to record the game.

How to use:
Download and install python if you don't already have python
1) Download python 2.7 at https://www.python.org/downloads/
2) Install it

Install dependency (requests)
3) Open terminal/command prompt and type : 
pip install requests

Getting lol api key to be able to call lol server
4) Login to lol at https://developer.riotgames.com/
5) Copy key

Run program
6) Type in terminal:
python stalker.py <key> <summoners ...> <options>
6+) 
(manditory) where <key> is the key you have copied from riot 
            where <summoners ...> is space separated names of summoners you want to monitor
            where <options> are additional options you can use
              check them out by typing:
                python stalker.py -h
6++) you can also specify your options using the settings.txt file
Open settings.txt and replace the values you want to replace
To add multiple summoners put comma-seperated names within quotes in the square brackets
