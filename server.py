from functools import wraps
from flask import Flask, session, redirect, url_for, escape, request, Response


#dev
from user import *
from switchs import *


app = Flask(__name__)


app.config['MYSQL_DATABASE_USER'] = 'domuspi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'domuspi'
app.config['MYSQL_DATABASE_DB'] = 'domuspi'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


# db = Db(app)

def islogged():
  return session['login'] == True

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if not islogged():
      return Response('Access Denied', 401)
    return f(*args, **kwargs)
  return decorated

@app.route("/")
def home():
  return "Follow <a href='https://github.com/hastrolaptecos/homeautomation'>https://github.com/hastrolaptecos/homeautomation</a>"

@app.route("/switch/<id>/state")
@requires_auth
def switch():
  return ""

@app.route("/switchs")
@requires_auth
def switchs():
  switchs = Switchs()
  ResponseController.json_response(switchs.get_all());

#############
@app.route("/auth/login")
def login():
  login = request.args.get('login')
  password = request.args.get('password')

  data = User().find_by_login(login)
  if data is None:
    return "Username is wrong."
  else: 
    print data
    if data['password'] == password:
      session['login'] = True
      session['_id'] = data['id']
      return "Logged in successfully."
    else:
      return "Password is wrong."

@app.route("/auth/logout")
def logout():
  session['login'] = False
  session['_id'] = None
  return 'see ya'


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
