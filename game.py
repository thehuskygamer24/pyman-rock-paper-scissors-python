import random
import time
import requests
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
print("use the input below to use 1 for rock 2 for paper 3 for scissors")
gamehub = ["rock","paper", "scissors", "paper","scissors","rock","scissors","paper","rock","rock","scissors","paper"]
p2 = requests.get("http://localhost:3007/accountget")
if p2 == "":
  pass
else:
 accountuser = p2.text.strip()
clientversion = "0.2.7"




def startgame():
 while True:
  
  userinput = float(input("1 2 3. "))
  try:
   requests.get("http://localhost:3007/update")
  
  
   time.sleep(3)
  except ConnectionError:
    print("game session logged out")
    time.sleep(3)
    print("unable to connect to a session code 3")
    time.sleep(10)
    print("server connection failed or no internet")
    startgameapproval = False
    time.sleep(300000)
  randomshoot = random.choice(gamehub)
  print("rock paper scissors")
  time.sleep(3)
 
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
    print("game has automaticly chose for you to avoid a crash")
   
    
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
   
  
  
    print("server connection successful you are signed in as "+ m1)
    print("your team Blue")
   else:
    print("server connection successful you are signed in as "+ p2.text)
    print("your team Blue")
 except ConnectionError:
   print("server connection failed or no internet")
   startgameapproval = False
   time.sleep(3000000)


print("welcome to pyman rock paper scissors")
time.sleep(1)
print("connecting to server")
serverconnect()
if startgameapproval == False:
  pass
  
else:
 time.sleep(4.3)
 startgame()

