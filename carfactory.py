from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, val):
  capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
  spindler_battery = SpindlerBattery(last_service_date, current_date)
  carrigan_tire = CarriganTire(val)

  car = Car(capulet_engine,spindler_battery, carrigan_tire)
  return car

def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, val):
  willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
  spindler_battery = SpindlerBattery(last_service_date, current_date)
  carrigan_tire = CarriganTire(val)

  car = Car(willoughby_engine,spindler_battery, carrigan_tire)
  return car

def create_palindrome(self, current_date, last_service_date, warning_light_on, val):
  sternman_engine = SternmanEngine(warning_light_on)
  spindler_battery = SpindlerBattery(last_service_date, current_date)
  carrigan_tire = CarriganTire(val)
  car = Car(sternman_engine,spindler_battery)
  return car

def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, val):
  willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
  nubbin_battery = NubbinBattery(last_service_date, current_date)
  octoprime_tire = OctoprimeTire(val)
  car = Car(willoughby_engine,nubbin_battery, octoprime_tire)
  return car

def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, val):
  capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
  nubbin_battery = NubbinBattery(last_service_date, current_date)

  octoprime_tire = OctoprimeTire(val)
  car = Car(capulet_engine,nubbin_battery, octoprime_tire)
  return car

  