from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá Anônimo!"

@app.route("/user/config")
def userconfig():
    return "Olá Usuário!"

@app.route("/admin/config")
def adminconfig():
    return "Olá Administrador!"
