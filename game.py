import random
import time
import requests
import os
from playsound import playsound
os.system("title Pyman RPS Cmd Game")
startgameapproval = True
from colorama import Fore,init
init(autoreset=True)
from requests.exceptions import ConnectionError
getgamestate = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/shutdownactivetxt")
getgamestatereason = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/shutdownreason.txt")
if getgamestate.text.strip() == "active":
  startgameapproval = False
  print(Fore.RED + "pyman RPS services are unavailable " + "reason: ", end='')
  print(Fore.LIGHTRED_EX + getgamestatereason.text.strip())
  time.sleep(3000000)
  exit()
else:
  pass

accountuser = "Blue Team"
print(Fore.YELLOW + "use the input below to use 1 for rock 2 for paper 3 for scissors")
gamehub = ["rock","paper", "scissors", "paper","scissors","rock","scissors","paper","rock","rock","scissors","paper"]
##if p2 == "":
  #pass
#else:
 #accountuser = p2.text.strip()
clientversion = "0.3.0"


def musicintro():
  playsound("soundtracks/westminsterintro2.mp3")

def startgame():
 while True:
  
  userinput = float(input(Fore.LIGHTBLUE_EX + "1 2 3. "))
  try:
   requests.get("http://192.168.1.65:3007/update")
  
  
   time.sleep(0.7)
  except ConnectionError:
    print(Fore.YELLOW + "game session logged out")
    time.sleep(3)
    print(Fore.RED + "unable to connect to a session code 3")
    time.sleep(10)
    print(Fore.RED + "server connection stopped unexpectly please relaunch the game and try again")
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
   requests.get("http://192.168.1.65:3007", timeout=7)
   c1 = requests.get("http://192.168.1.65:3007/version")
   if c1.text == clientversion:
    pass
   else:
     print(Fore.RED + "client outdated please update the software https://github.com/thehuskygamer24/pyman-rock-paper-scissors-python")
     print(Fore.YELLOW + "be aware the client will not bypass the update requirement")
     print(Fore.YELLOW + "if there is an issue with updating pyman or version not set correctly between the client server or both then please contact @supersaiyanslasher on discord the owner of the game")
     startgameapproval = False
     time.sleep(30000)
   time.sleep(3)
   if accountuser == "":
    print("you need to create your userid")
    m1 = input("").strip()
    requests.post("http://192.168.1.65:3007/accountadd", data=m1)
   
  
  
    print(Fore.GREEN + "server connection successful you are signed in as "+ "Blue Team")
    print(Fore.BLUE + "your team Blue")
   else:
    print(Fore.GREEN + "server connection successful you are signed in as "+ "Blue Team")
    print(Fore.BLUE + "your team Blue")
 except ConnectionError:
   print(Fore.RED + "failed to connect to RPS.NET error code: outage")
   startgameapproval = False
   time.sleep(3000000)


print(Fore.BLUE + "welcome to pyman rock paper scissors")
time.sleep(1)
print(Fore.CYAN + "connecting to server")
serverconnect()
if startgameapproval == False:
  pass
  
else:
 time.sleep(1)
 
 musicintro()
 time.sleep(3)
 startgame()
 print("your command pallet has been enabled have fun :)")

