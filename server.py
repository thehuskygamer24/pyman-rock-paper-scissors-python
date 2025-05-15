from flask import Flask 
app = Flask(__name__)
serverversion = "0.2.3"
@app.route("/")
def connectivity():
  return "connection success"
@app.route("/version")
def version():
  return serverversion
@app.route("/update")
def heartbeat():
  return "heartbeat1"
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=3007)
