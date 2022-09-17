import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
  def should_be_serviced(self):
    last_service_date= datetime.datetime(2012,6,2)
    current_date = datetime.datetime(2019,5,9)
    battery = NubbinBattery(last_service_date, current_date)
    self.assertTrue(battery.needs_service())

  def should_not_be_serviced(self):
    last_service_date= datetime.datetime(2012,6,2)
    current_date = datetime.datetime(2013,9,9)
    battery = NubbinBattery(last_service_date, current_date)
    self.assertFalse(battery.needs_service())




class TestSpindlerBattery(unittest.TestCase):
  def should_be_serviced(self):
    last_service_date= datetime.datetime(2012,6,2)
    current_date = datetime.datetime(2014,5,9)
    battery = SpindlerBattery(last_service_date, current_date)
    self.assertTrue(battery.needs_service())

  def should_not_be_serviced(self):
    last_service_date= datetime.datetime(2012,6,2)
    current_date = datetime.datetime(2013,9,9)
    battery = SpindlerBattery(last_service_date, current_date)
    self.assertFalse(battery.needs_service())