import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
  def should_be_serviced(self):
    val = [0.2,0.5,0.9,0.6]
    tire = CarriganTire(val)
    self.assertTrue(tire.needs_service())

  def should_not_be_serviced(self):
    val = [0.2,0.5,0.2,0.6]
    tire = CarriganTire(val)
    self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
  def should_be_serviced(self):
    val = [0.7,0.8,0.9,0.8]
    tire = OctoprimeTire(val)
    self.assertTrue(tire.needs_service())

  def should_not_be_serviced(self):
    val = [0.1,0.2,0.9,0.6]
    tire = OctoprimeTire(val)
    self.assertFalse(tire.needs_service())
