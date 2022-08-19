from flask import Flask, jsonify, request
import samino
app = Flask(__name__)

@app.route('/')
def homepage():
  
  return'Api working!'
  
@app.route('/login', methods = ['POST'])
def teste_endpoint():
  data = request.form
  email = data["email"]
  password = data["password"]
  device = data["device"]
  client = samino.Client(device)
  sid = client.login(email,password).sid
  return jsonify(sid)
