import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
  def should_be_serviced(self):
    current_mileage = 60000
    last_service_mileage = 2000
    engine = CapuletEngine(current_mileage,last_service_mileage)
    self.assertTrue(engine.needs_service())

  def should_not_be_serviced(self):
    current_mileage = 30000
    last_service_mileage = 0
    engine = CapuletEngine(current_mileage,last_service_mileage)
    self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
  def should_be_serviced(self):
    warning_light_is_on = True
    engine = SternmanEngine(warning_light_is_on)
    self.assertTrue(engine.needs_service())

  def should_not_be_serviced(self):
    warning_light_is_on = False
    engine = SternmanEngine(warning_light_is_on)
    self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
  def should_be_serviced(self):
    current_mileage = 80000
    last_service_mileage = 2000
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    self.assertTrue(engine.needs_service())

  def should_not_be_serviced(self):
    current_mileage = 60000
    last_service_mileage = 0
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    self.assertFalse(engine.needs_service())

