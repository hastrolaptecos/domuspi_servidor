from db import *


class User(Db):

  def find_by_login(self, login):
    query = "SELECT * FROM users where login='" + login + "'"
    print query;
    return self.query_one(query)
  
  def find_by_id(self, id):
    return self.query_one("SELECT * FROM users where id='" + id + "'")
