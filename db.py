import MySQLdb 

 
dsn = {
  'user':'domuspi',
  'password':'domuspi',
  'db':'domuspi',
  'host':'localhost',
}

class Db(object):

  cursor = None

  def __init__(self):
    
    self.db = dsn['db']
    self.host = dsn['host']
    self.user = dsn['user']
    self.password = dsn['password']

    self.connect()
    self.set_db()
    self.charge_cursor()

  def connect(self):
    try:
      self.mysql = MySQLdb.connect(self.host, self.user, self.password)
    except MySQLdb.Error, e:
      print "DB CONNECTION ERROR", e

  def set_db(self):
    self.mysql.select_db(self.db)

  def disconnection(self):
    self.mysql.close()

  def charge_cursor(self):
    if self.cursor is None:
      self.cursor = self.mysql.cursor(MySQLdb.cursors.DictCursor)

  def query_one(self, query):
    self.cursor.execute(query)
    rs = self.cursor.fetchone()
    self.disconnection()
    return rs
  
  def query(self, query):
    self.cursor.execute(query)
    rs =  self.cursor.fetchall()
    self.disconnection()
    return rs

  def update(self, query):
    self.cursor.execute(query)
    rs =  self.cursor.commit()
    self.disconnection()
