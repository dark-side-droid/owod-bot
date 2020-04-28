oWoD-Bot written by dark-side-droid.


## Introduction

This is an bot whose purpose is to act as an assistant to players and storytellers playing
Vampire:The Masquerade (v20) games and/or Mage: The Ascension with the aim of making tedious acts like
rolling dice go faster, so that everyone can spend their time focusing on the game and their actions, 
instead of waiting around while someone finds the specific page in a book somewhere or counting his 10's and 1's in a dice pool.

It was written during the first days of the coronavirus pandemic(COVID-19) and the ensuing lockdowns when we had to transfer our oWoD RPG
online and we were looking for the best solution. Since we already use discord heavily that choice made sense, but after
completing our first session it was obvious that the logistics of things slowed down the game heavily, since some players preferred rolling their
own dice but we could not agree upon a fair-for-all method of doing that.

At its inception this was intented to be a dice rolling bot with a focus on 10 sided dice that could assist us in our
complicated rolls for our Crossover game between Vampires and Mages, but found extra uses as a repository of on-demand text
and systems for the various supernatural powers these creatures hold or other game mechanics.

Currently it contains a dice rolling system which accounts for 1s, information on most of the vampiric disciplines and magical spheres, paths of enlightenment,
information on the blood bond and the dreaded diablerie and a bit of what i consider to be..humour.
Soon it will be complete, containing Elder disciplines, bloodlines and bloodline-specific powers, the Roads of Dark Ages:Vampire and the few paths of enlightenment
outside them, Archspheres as well as information and rules on spellcasting and paradox.

It does not contain merits and flaws from any game, Thaumaturgy,Necromancy or any sort of Sorcery powers or rituals, Nature/Demeanors, Avatar essences
or resonance rules and does not account for double successes from Specialties, you'll have to do that yourself for now.



## Dependencies
* Python 3
* Discord.py
* A code editor
* A bot application

## How to Setup
* Install python3 if you dont already have it
* Create the bot(https://realpython.com/how-to-make-a-discord-bot-python/)
* Add your bot's token inside Bot.py using the editor of your choice
* Download discord.py from pypi (https://pypi.org/project/discord.py/)
* run CMD as administrator
* cd in the folder that you downloaded discord.py and then:
* py -m pip install -U discord.py
* After setup is complete run Bot.py

## Commands
After the bot is online, simply type 'bot commands' into chat and it will reply with a list of available commands and an example for each one.

In addition you can PM the any command to the bot and it will directly PM its response to said command back to you. Useful in case you want a command to be hidden.

To roll dice type 'roll dice' followed by the number of dice,the difficulty for the roll. For example let us suppose that you want to roll 15 dice versus a difficulty of 8. Type into the chat 'roll dice  15,8'.

To get information on any discipline type get followed by the discipline name and the corresponding level. For example : 'get dominate 1'.



