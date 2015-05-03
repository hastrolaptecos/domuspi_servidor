from flaskext.mysql import MySQL

class Db(object):

  cursor = None

  def __init__(self, app):
    self.mysql = MySQL() 
    self.mysql.init_app(app)
    self.charge_cursor()
  
  def charge_cursor(self):
    if self.cursor is None:
      self.cursor = self.mysql.connect().cursor()

  def query_one(self, query):
    self.cursor.execute(query)
    return self.cursor.fetchone()


  def find_user_by_login(self, login):
    query = "SELECT * FROM users where login='" + login + "'"
    print query;
    return self.query_one(query)
  
  def find_user_by_id(self, id):
    return self.query_one("SELECT * FROM users where id='" + id + "'")
