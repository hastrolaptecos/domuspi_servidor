import sys
sys.path.insert(0, 'lib/')

import Adafruit_MCP230xx
from db import *

bus_controller = Adafruit_MCP230xx.Adafruit_MCP230XX(address = 0x20, num_gpios = 16)

class SwitchController:

  ON = 1
  OFF = 0

  def __init__(self, id):

    self.switch_db = Switchs()
  
    self.switch_data = self.switch_db.find_by_id(id)
    
    self.GPIO_pin = self.switch_data['code']
    
    self.setup_controller();

  def setup_controller(self):
    self.gpio_controller = bus_controller
    self.set_output()

  def set_output(self):
    self.gpio_controller.config(self.GPIO_pin, self.gpio_controller.OUTPUT)
  
  def on(self):
    self.switch_db.update_state(self.switch_data['id'], self.ON)    
    self.gpio_controller.output(self.GPIO_pin, self.ON)

  def off(self):
    self.switch_db.update_state(self.switch_data['id'], self.OFF)    
    self.gpio_controller.output(self.GPIO_pin, self.OFF)


class Switchs(Db):

  def find_by_id(self, id):
    return self.query_one("SELECT * FROM switchs where id = '" + str(id) + "'")

  def update_state(self,id,state):
    return self.update("UPDATE switchs SET state = " + str(state) + " WHERE id = '" + str(id) + "'")

  def get_all(self):
    return self.query("SELECT * FROM switchs")


class ResetSwitchs:
  @staticmethod
  def resetAll():
    switch_db = Switchs()
    switchs = switch_db.get_all();
    for switch in switchs:
      switch_db.update_state(switch['id'],0)