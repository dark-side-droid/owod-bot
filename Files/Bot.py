import discord
import random
from disciplines import *
from spheres import *
from mybotfuncs import *
from Roads import *
from v20_misc import *


TOKEN = "NjkyNzkxODIwMTY5NzczMTI2.XnzqqQ.O1n9rizsv5LYDg7pFcq9Raf5bqU"
client = discord.Client()



#Terminal message that tells you the bot is logged in
@client.event
async def on_ready():
    print ("oWoD Bot written by dark-side-droid")
    print('We have logged in as {0.user}'.format(client))
    


#Bot functions
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #INTERACTION AND FUN 

    if message.content.startswith("hello ravanna"):
        await message.channel.send("How dare you try and talk to me! I will devour your blood and your soul ! As soon as i am finished eating breakfast.")

    if message.content.startswith("ravanna") or message.content.startswith("RAVANNA"):
        await message.channel.send("STOP SPEAKING MY UNHOLY NAME ! I AM RESTING !")

    if message.content.startswith("ravanna what is paradox?") or message.content.startswith("Ravanna what is paradox?"):
        await message.channel.send("There is only one kind of paradox and that is the path of paradox")

    #BOT COMMANDS 
    if message.content.startswith("bot commands") or message.content.startswith("RAVANNA HELP"):
        helptext = botcommands()
        await message.channel.send(helptext)

    #DICE ROLLER


    if message.content.startswith("roll dice"):
        print (message.content[:])
        playertext = message.content[:]
        playertext = stringreplacer(playertext)
        myroll = rolldice(playertext[0],playertext[1])
        await message.channel.send(myroll[0])
        await message.channel.send(myroll[1])
        await message.channel.send(myroll[2])


    #VAMPIRIC DISCIPLINES
        

    if message.content.startswith("get dominate 1"):
        disciplinetext = getdiscipline("dominate1")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dominate 2"):
        disciplinetext = getdiscipline("dominate2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dominate 3"):
        disciplinetext = getdiscipline("dominate3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get dominate 4"):
        disciplinetext = getdiscipline("dominate4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get dominate 5"):
        disciplinetext = getdiscipline("dominate5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get quietus 1"):
        disciplinetext = getdiscipline("quietus1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get quietus 2"):
        disciplinetext = getdiscipline("quietus2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get quietus 3"):
        disciplinetext = getdiscipline("quietus3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get quietus 4"):
        disciplinetext = getdiscipline("quietus4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get quietus 5"):
        disciplinetext = getdiscipline("quietus5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get obfuscate 1"):
        disciplinetext = getdiscipline("obfuscate1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get obfuscate 2"):
        disciplinetext = getdiscipline("obfuscate2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get obfuscate 3"):
        disciplinetext = getdiscipline("obfuscate3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get obfuscate 4"):
        disciplinetext = getdiscipline("obfuscate4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        
    if message.content.startswith("get obfuscate 5"):
        disciplinetext = getdiscipline("obfuscate5")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get obtenebration 1"):
        disciplinetext = getdiscipline("obtenebration1")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get obtenebration 2"):
        disciplinetext = getdiscipline("obtenebration2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
       
    if message.content.startswith("get obtenebration 3"):
        disciplinetext = getdiscipline("obtenebration3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get obtenebration 4"):
        disciplinetext = getdiscipline("obtenebration4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get obtenebration 5"):
        disciplinetext = getdiscipline("obtenebration5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    #AUSPEX CLASH OF WILLS
    if message.content.startswith("auspexclash"):
        disciplinetext = getdiscipline("auspexclash")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])
        await message.channel.send(disciplinetext[3])

    if message.content.startswith("get auspex 1"):
        disciplinetext = getdiscipline("auspex1")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])
        await message.channel.send(disciplinetext[3])
        await message.channel.send(disciplinetext[4])

    if message.content.startswith("get auspex 2"):
        disciplinetext = getdiscipline("auspex2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])
        await message.channel.send(disciplinetext[3])
        await message.channel.send(disciplinetext[4])

    if message.content.startswith("get auspex 3"):
        disciplinetext = getdiscipline("auspex3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])
        await message.channel.send(disciplinetext[3])
        await message.channel.send(disciplinetext[4])

    if message.content.startswith("get auspex 4"):
        disciplinetext = getdiscipline("auspex4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])

    if message.content.startswith("get auspex 5"):
        disciplinetext = getdiscipline("auspex5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])
        await message.channel.send(disciplinetext[2])
        await message.channel.send(disciplinetext[3])

    if message.content.startswith("get chimerstry 1"):
        disciplinetext = getdiscipline("chimerstry1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get chimerstry 2"):
        disciplinetext = getdiscipline("chimerstry2")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get chimerstry 3"):
        disciplinetext = getdiscipline("chimerstry3")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get chimerstry 4"):
        disciplinetext = getdiscipline("chimerstry4")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get chimerstry 5"):
        disciplinetext = getdiscipline("chimerstry5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dementation 1"):
        disciplinetext = getdiscipline("dementation1")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dementation 2"):
        disciplinetext = getdiscipline("dementation2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dementation 3"):
        disciplinetext = getdiscipline("dementation3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dementation 4"):
        disciplinetext = getdiscipline("dementation4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get dementation 5"):
        disciplinetext = getdiscipline("dementation5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get presence 1"):
        disciplinetext = getdiscipline("presence1")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get presence 2"):
        disciplinetext = getdiscipline("presence2")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get presence 3"):
        disciplinetext = getdiscipline("presence3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get presence 4"):
        disciplinetext = getdiscipline("presence4")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get presence 5"):
        disciplinetext = getdiscipline("presence5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get protean 1"):
        disciplinetext = getdiscipline("protean1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get protean 2"):
        disciplinetext = getdiscipline("protean2")
        await message.channel.send(disciplinetext)
 
    if message.content.startswith("get protean 3"):
        disciplinetext = getdiscipline("protean3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get protean 4"):
        disciplinetext = getdiscipline("protean4")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get serpentis 1"):
        disciplinetext = getdiscipline("serpentis1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get serpentis 2"):
        disciplinetext = getdiscipline("serpentis2")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get serpentis 3"):
        disciplinetext = getdiscipline("serpentis3")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get serpentis 4"):
        disciplinetext = getdiscipline("serpentis4")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get serpentis 5"):
        disciplinetext = getdiscipline("serpentis5")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get vicissitude 1"):
        disciplinetext = getdiscipline("vicissitude1")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get vicissitude 2"):
        disciplinetext = getdiscipline("vicissitude2")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get vicissitude 3"):
        disciplinetext = getdiscipline("vicissitude3")
        await message.channel.send(disciplinetext[0])
        await message.channel.send(disciplinetext[1])

    if message.content.startswith("get vicissitude 4"):
        disciplinetext = getdiscipline("vicissitude4")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get vicissitude 5"):
        disciplinetext = getdiscipline("vicissitude5")
        await message.channel.send(disciplinetext)

    if message.content.startswith("get vicissitude 6"):
        disciplinetext = getdiscipline("vicissitude6")
        await message.channel.send(disciplinetext)

    #PATHS OF ENLIGHTENMENT 
    if message.content.startswith("get road of blood"):
        roadtext = getroad("road of blood")
        await message.channel.send(roadtext)

    if message.content.startswith("get road of bones"):
        roadtext = getroad("road of bones")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of caine"):
        roadtext = getroad("path of caine")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of cathari"):
        roadtext = getroad("path of cathari")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of feral heart"):
        roadtext = getroad("path of feral heart")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of honorable accord"):
        roadtext = getroad("path of honorable accord")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of lilith"):
        roadtext = getroad("path of lilith")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of metamorphosis"):
        roadtext = getroad("path of metamorphosis")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of night"):
        roadtext = getroad("path of night")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of paradox"):
        roadtext = getroad("path of paradox")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of power and the inner voice"):
        roadtext = getroad("path of power and the inner voice")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of typhon"):
        roadtext = getroad("path of typhon")
        await message.channel.send(roadtext)

    if message.content.startswith("get path of humanity"):
        roadtext = getroad("path of humanity")
        await message.channel.send(roadtext)

    if message.content.startswith("get road list"):
        roadtext = getroad("get road info")
        await message.channel.send(roadtext)

    #GET MISC INFO 
    if message.content.startswith("get blood bond"):
        miscinfo = getmiscinfo("get blood bond")
        await message.channel.send(miscinfo[0])
        await message.channel.send(miscinfo[1])
        await message.channel.send(miscinfo[2])
        await message.channel.send(miscinfo[3])
        await message.channel.send(miscinfo[4])

    if message.content.startswith("get diablerie"):
        miscinfo = getmiscinfo("get diablerie")
        await message.channel.send(miscinfo[0])
        await message.channel.send(miscinfo[1])
        await message.channel.send(miscinfo[2])
        await message.channel.send(miscinfo[3])
        await message.channel.send(miscinfo[4])
        await message.channel.send(miscinfo[5])
        await message.channel.send(miscinfo[6])





      


    #MAGE SPHERES FROM HERE

    if message.content.startswith("get life 1"):
        spheretext = getsphere("life1")
        await message.channel.send(spheretext)

    if message.content.startswith("get life 2"):
        spheretext = getsphere("life2")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get life 3"):
        spheretext = getsphere("life3")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get life 4"):
        spheretext = getsphere("life4")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get life 5"):
        spheretext = getsphere("life5")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get spirit 1"):
        spheretext = getsphere("spirit1")
        await message.channel.send(spheretext)

    if message.content.startswith("get spirit 2"):
        spheretext = getsphere("spirit2")
        await message.channel.send(spheretext)

    if message.content.startswith("get spirit 3"):
        spheretext = getsphere("spirit3")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get spirit 4"):
        spheretext = getsphere("spirit4")
        await message.channel.send(spheretext)

    if message.content.startswith("get spirit 5"):
        spheretext = getsphere("spirit5")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get prime 1"):
        spheretext = getsphere("prime1")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])
   
    if message.content.startswith("get prime 2"):
        spheretext = getsphere("prime2")
        await message.channel.send(spheretext)

    if message.content.startswith("get prime 3"):
        spheretext = getsphere("prime3")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get prime 4"):
        spheretext = getsphere("prime4")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get prime 5"):
        spheretext = getsphere("prime5")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    if message.content.startswith("get entropy 1"):
        spheretext = getsphere("entropy1")
        await message.channel.send(spheretext)

    if message.content.startswith("get entropy 2"):
        spheretext = getsphere("entropy2")
        await message.channel.send(spheretext)

    if message.content.startswith("get entropy 3"):
        spheretext = getsphere("entropy3")
        await message.channel.send(spheretext)
        
    if message.content.startswith("get entropy 4"):
        spheretext = getsphere("entropy4")
        await message.channel.send(spheretext)
        
    if message.content.startswith("get entropy 5"):
        spheretext = getsphere("entropy5")
        await message.channel.send(spheretext[0])
        await message.channel.send(spheretext[1])

    
    


client.run(TOKEN)

