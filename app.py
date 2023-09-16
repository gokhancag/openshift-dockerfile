import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Selamlar OpenShift with <b>Dockerfile!</b>"

@app.route('/nasilsin')
def nasilsin():
    return 'iyiyim, sen nasilsin?'

@app.route('/hello')
def hello():
    return 'hello from OpenShift with Dockerfile..'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)