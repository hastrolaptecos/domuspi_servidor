import sys
sys.path.insert(0, 'lib/')

import Adafruit_MCP230xx
from db import *

class SwitchController:

  ON = 1
  OFF = 0

  def __init__(self, id):

    self.switch_db = Switchs()
  
    self.switch_data = self.switch_db.find_by_id(id)
    
    self.GPIO_pin = self.switch_data[code]
  
  def setup_controller(self):
    self.gpio_controller = Adafruit_MCP230xx.Adafruit_MCP230XX(address=0x20, num_gpios=16)

  def set_output(self):
    self.gpio_controller.config(self.GPIO_pin, self.gpio_controller.OUTPUT)
  
  def on(self):
    self.output(self.GPIO_pin,self.ON)

  def off(self):
    self.output(self.GPIO_pin,self.OFF)


class Switchs(Db):

  def find_by_id(self, id):
    return self.query_one("SELECT * FROM switchs where id = '" + id + "'")

  def update_state(self,id,state):
    return self.query_one("UPDATE switchs SET state = '" + state + "' where id = '" + id + "'")

  def get_all(self):
    return self.query("SELECT * FROM switchs")
