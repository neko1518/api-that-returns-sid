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
  senha = data["senha"]
  device = data["device"]
  #sid =samino.Client().login(email,senha).sid

  return jsonify(email)
