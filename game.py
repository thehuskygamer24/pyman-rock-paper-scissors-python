import random
import time
import requests
import os
os.system("title Pyman RPS Cmd Game")
startgameapproval = True
from colorama import Fore,init
init(autoreset=True)
from requests.exceptions import ConnectionError
getgamestate = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/serverstat.txt")
getgamestatereason = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/shutdownreason.txt")
if getgamestate.text.strip() == "true":
  startgameapproval = False
  print(Fore.RED + "game services are offline " + "reason: ", end='')
  print(Fore.YELLOW + getgamestatereason.text.strip())
  time.sleep(3000000)
else:
  pass

accountuser = ""
print(Fore.YELLOW + "use the input below to use 1 for rock 2 for paper 3 for scissors")
gamehub = ["rock","paper", "scissors", "paper","scissors","rock","scissors","paper","rock","rock","scissors","paper"]
p2 = requests.get("http://localhost:3007/accountget")
if p2 == "":
  pass
else:
 accountuser = p2.text.strip()
clientversion = "0.3.0"




def startgame():
 while True:
  
  userinput = float(input(Fore.LIGHTBLUE_EX + "1 2 3. "))
  try:
   requests.get("http://localhost:3007/update")
  
  
   time.sleep(0.7)
  except ConnectionError:
    print(Fore.YELLOW + "game session logged out")
    time.sleep(3)
    print(Fore.RED + "unable to connect to a session code 3")
    time.sleep(10)
    print(Fore.RED + "server connection failed or no internet")
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
   requests.get("http://localhost:3007", timeout=7)
   c1 = requests.get("http://localhost:3007/version")
   if c1.text == clientversion:
    pass
   else:
     print("client outdated please update the software https://github.com/thehuskygamer24/pyman-rock-paper-scissors-python")
     startgameapproval = False
     time.sleep(30000)
   time.sleep(3)
   if accountuser == "":
    print("you need to create your userid")
    m1 = input("").strip()
    requests.post("http://localhost:3007/accountadd", data=m1)
   
  
  
    print(Fore.GREEN + "server connection successful you are signed in as "+ m1)
    print(Fore.BLUE + "your team Blue")
   else:
    print(Fore.GREEN + "server connection successful you are signed in as "+ p2.text)
    print(Fore.BLUE + "your team Blue")
 except ConnectionError:
   print(Fore.RED + "server connection failed or no internet")
   startgameapproval = False
   time.sleep(3000000)


print(Fore.BLUE + "welcome to pyman rock paper scissors")
time.sleep(1)
print(Fore.CYAN + "connecting to server")
serverconnect()
if startgameapproval == False:
  pass
  
else:
 time.sleep(4.3)
 startgame()

