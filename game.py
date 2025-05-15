import random
import time
import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
print("use the input below to use 1 for rock 2 for paper 3 for scissors")
gamehub = ["rock","paper", "scissors", "paper","scissors","rock","scissors","paper","rock","rock","scissors","rock"]

startgameapproval = True
def startgame():
 while True:
  userinput = float(input("1 2 3. "))
  try:
   requests.get("https://0a526b55-53a3-4399-abef-136348916a3b-00-16ciu3enkb4nk.picard.replit.dev/update",timeout=7)
  except Timeout:
    print("Please Log Back in again")
    time.sleep(3)
    print("server stopped unexpectly")
    print("if server issue presists contact the owner of the game or support")
    time.sleep(3000000)
  except ConnectionError:
    print("no internet connection please check your internet and try again")
    startgameapproval = False
    time.sleep(300000)
  randomshoot = random.choice(gamehub)
  print("rock paper scissors")
  time.sleep(3)
 
  if userinput == 1:
     print("your response rock")
  elif userinput == 2:
     print("your response paper")
  elif userinput == 3:
    print("your response scissors")
  print("cpu's response " + randomshoot)
def serverconnect():
 try:
   requests.get("https://0a526b55-53a3-4399-abef-136348916a3b-00-16ciu3enkb4nk.picard.replit.dev/", timeout=7)
   time.sleep(10)
   print("server connection successful you are signed in as a guest")
 except Timeout:
   print("theres no active server connection")
   startgameapproval = False
   time.sleep(30000)
 except ConnectionError:
   print("no internet connection please check your internet and try again")
   startgameapproval = False
   time.sleep(3000000)


print("welcome to pyman rock paper scissors")
time.sleep(3)
print("connecting to server")
serverconnect()
if startgameapproval == False:
  pass
else:
 time.sleep(8)
 startgame()

