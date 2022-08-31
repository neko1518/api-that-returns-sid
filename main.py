from flask import Flask,request
import samino
app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def login():
  data = request.form
  email = data["email"]
  password = data["password"]
  device = data["device"]
  client = samino.Client(device)
  x = client.login(email,password)
  return x
