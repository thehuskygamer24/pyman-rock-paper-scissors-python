import random
import time
print("WELCOME TO ROCK PAPER SCISSORS.PY")
print("use the input below to use 1 for rock 2 for paper 3 for scissors")
gamehub = ["rock","paper", "scissors", "rock","paper", "scissors","rock","paper", "scissors"]



while True:
 userinput = float(input("1 2 3. "))
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