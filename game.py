import random
import time
import requests
import os

from playsound import playsound
os.system("title Pyman RPS")
startgameapproval = True
from colorama import Fore

from requests.exceptions import ConnectionError






print(Fore.YELLOW + "use the input below to use 1 for rock 2 for paper 3 for scissors and then 4 to return to menu")
gamehub = ["rock","paper", "scissors", "paper","scissors","rock","scissors","paper"]



clientversion = "0.3.5"
pathr = "system/New folder (7)/fgdt.txt"
b6 =open(pathr)
b7 = b6.read()
if not b7 == "":
  pass
  
else:
 
 cms = random.randint(1,100000)

 

 cm = open(pathr, "w")
 cm.write(str(cms))
 cm.close()


def musicintro():
  playsound("soundtracks/5h.mp3")

def startgame():
 while True:
  
  userinput = float(input(Fore.LIGHTBLUE_EX + "1 2 3 4. "))
  try:
   requests.get("https://45.23.232.171:3007/update",verify='auth/cert.pem')
  
  
   time.sleep(0.7)
  except ConnectionError:
    print(Fore.YELLOW + "game session logged out")
    time.sleep(3)
    print(Fore.RED + "no active server connection session code 3")
    time.sleep(10)
    print(Fore.RED + "server connection reset changed or shutdown unexpectly please relaunch the game and try again")
    startgameapproval = False
    time.sleep(300000)
  randomshoot = random.choice(gamehub)
  print("rock paper scissors")
  time.sleep(1)
 
  if userinput == 1:
     print(Fore.BLUE + "your response rock")
  elif userinput == 2:
     print(Fore.BLUE + "your response paper")
  elif userinput == 3:
    print(Fore.BLUE + "your response scissors")
  elif userinput == 4:
    print("returning to main menu. ")
    returntime = random(float(1,2,3,5))
    time.sleep(returntime)
  else:
    print("option invalid")
    avoidcrashplrshoot = random(float(1,2,3))
    if avoidcrashplrshoot == 1:
      print("rock")
    elif avoidcrashplrshoot == 2:
      print("paper")
    elif avoidcrashplrshoot == 3:
      print("scissors")
      
    else:
      print("auto shoot failed")
    print(Fore.YELLOW + "game has automaticly chose for you to avoid a crash")
   
    
  print(Fore.RED + "cpu's response " + randomshoot)

def serverconnect():
 try:
   requests.get("https://45.23.232.171:3007", verify='auth/cert.pem')
   c1 = requests.get("https://45.23.232.171:3007/version", verify='auth/cert.pem')
   
   if c1.text == clientversion:
    pass
   else:
     print(Fore.RED + "client outdated please update the software https://github.com/thehuskygamer24/pyman-rock-paper-scissors-python")
     print(Fore.LIGHTRED_EX + "be aware the client will not bypass the update requirement")
     print(Fore.LIGHTRED_EX + "if there is an issue with updating pyman or version not set correctly between the client server or both then please contact @supersaiyanslasher on discord the owner of the game")
     startgameapproval = False
     time.sleep(30000)
   time.sleep(1)
 
   
   try:
     requests.get("https://45.23.232.171:3007/tempprofile",verify='auth/cert.pem')
   except ConnectionError:
     print(Fore.RED + "Failed to log into session-profile: Code 2")
     time.sleep(30000)
  
   print(Fore.LIGHTYELLOW_EX + "server connection successful you are signed in as "+ "Player Blue")
   print(Fore.BLUE + "your team Blue")
   
 except ConnectionError:
   print(Fore.RED + "failed to connect to RPS.NET error code: outage")
   startgameapproval = False
   time.sleep(3000000)
 
def mainmenu():
  
  print(Fore.LIGHTGREEN_EX + "(1) Play Game")
  print(Fore.LIGHTGREEN_EX + "(2) Shutdown Game")
  print(Fore.LIGHTGREEN_EX + "(3) Gallery")
  print(Fore.LIGHTGREEN_EX + "(4) Staff contact")
  print(Fore.LIGHTGREEN_EX + "(5) Update Log")
  print(Fore.LIGHTGREEN_EX + "(6) Settings")
  vm1 = input('')
  if vm1 == '1':
    print(Fore.CYAN + "Its Game Time")
    time.sleep(3)
    print(Fore.LIGHTGREEN_EX + "your command pallet has been enabled have fun :)")
    startgame()
  elif vm1 == '2':
    exit()
  elif vm1 == "3":
    print("(1) Top wins")
    print("(2) ultimate users who played")
    print("by discord username")
    
    print("gallery update coming soon")
    input("back. ")
    mainmenu()
  elif vm1 == "4":
    print("contact staff at https://discord.gg/CCMyCN2qBR")

    input("back. ")
    mainmenu()
  elif vm1 == "5":
    bm1 = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/update.txt")
    print(bm1.text.strip())
    input("back. ")
    mainmenu()
  elif vm1 == "6":
    print("settings feature coming soon")
    time.sleep(3)
    mainmenu()
  else:
    pass

print(Fore.BLUE + "welcome to pyman rock paper scissors")
time.sleep(1)
print(Fore.CYAN + "connecting to server")
serverconnect()


if startgameapproval == False:
  pass
  
else:

 
 
 mainmenu()
 time.sleep(3)
 



