from flask import Flask, request
import requests
app = Flask(__name__)
y1 = requests.get("https://raw.githubusercontent.com/thehuskygamer24/pyman-rock-paper-scissors-python/refs/heads/main/version.txt")
serverversion = y1

@app.route("/")
def connectivity():
  return "connection success"
@app.route("/version")
def version():
  return serverversion
@app.route("/update")
def heartbeat():
  return "heartbeat1"
@app.route("/accountadd", methods = ["POST"])
def grabaccount():
  b1 = request.data.decode("utf-8")
  with open("serveruser.txt", "a") as c7:


   c7.write(b1)
  return "." 
@app.route("/accountget")
def sendaccount():
  v1 = open("serveruser.txt")
  v2 = v1.read()
  if v1 == "":
    return ""
  else:
   return v2


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=3007)
