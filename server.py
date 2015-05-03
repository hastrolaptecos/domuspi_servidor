from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Follow <a href='https://github.com/hastrolaptecos/homeautomation'>https://github.com/hastrolaptecos/homeautomation</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')