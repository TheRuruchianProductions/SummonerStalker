# SummonerStalker
Puts a big brother on a set of summoners, recording them whenever they are in a game.

Description:
A console program running on python that will poll riot api server for current games of several summoners. If they are inside a game the program will contact op.gg to record the game.

<br>How to use:
<br>Download and install python if you don't already have python
<br>1) Download python 2.7 at https://www.python.org/downloads/ <br>
<br>2) Install it
<br>
<br>Install dependency (requests)
<br>3) Open terminal/command prompt and type : 
<br>pip install requests
<br>
<br>Getting lol api key to be able to call lol server
<br>4) Login to lol at https://developer.riotgames.com/
<br>5) Copy key
<br>
<br>Run program
<br>6) Type in terminal:
<br>python stalker.py <key> <summoners ...> <options>
<br>6+) 
<br>(manditory) where <key> is the key you have copied from riot 
<br>            where <summoners ...> is space separated names of summoners you want to monitor
<br>            where <options> are additional options you can use
<br>              check them out by typing:
<br>                python stalker.py -h
<br>6++) you can also specify your options using the settings.txt file
<br>Open settings.txt and replace the values you want to replace
<br>To add multiple summoners put comma-seperated names within quotes in the square brackets
