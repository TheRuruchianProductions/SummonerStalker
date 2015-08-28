# SummonerStalker
Puts a big brother on a set of summoners, recording them whenever they are in a game.

Description:
A console program running on python that will poll riot api server for current games of several summoners. If they are inside a game the program will contact op.gg to record the game.

<br>How to use:
<b><i>Download and install python if you don't already have python</i></b>
<ol>
<li> Download python 2.7 at https://www.python.org/downloads/
<li> Install it
</ol>
<b><i>Install dependency (requests)</i></b>
<ol>
<li> Open terminal/command prompt and type :<br><i>pip install requests</i>
</ol>
<b><i>Getting lol api key to be able to call lol server</i></b>
<ol>
<li> Login to lol at https://developer.riotgames.com/
<li> Copy key
</ol>
<b><i>Run program</i></b>
<ol>
<li> Type in terminal:<br><i>python stalker.py [key] [summoners ...] [options]</i>
<ul>
            <li>where [key] is the key you have copied from riot (manditory)
            <li>where [summoners ...]  is space separated names of summoners you want to monitor
            <li>where [options] are additional options you can use
            <li>check them out by typing:<i>python stalker.py -h</i>
</ul>
<li> You can also specify your options using the settings.txt file
<ul>
      <li>Open settings.txt and replace the values you want to replace
      <li>Add multiple summoners by putting comma-seperated names within quotes in the square brackets
</ul>
</ol>

