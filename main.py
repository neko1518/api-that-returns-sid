from flask import Flask, jsonify, request
import samino
app = Flask(__name__)

@app.route('/')
def homepage():
  
  return'essa é minha homepage'
  
@app.route('/teste', methods = ['POST'])
def teste_endpoint():
  data = request.form
  email = data["email"]
  password = data["senha"]
  device = data["device"]
  client = samino.Client(device)
  sid = client.login(email,password).sid
  return jsonify(sid)
