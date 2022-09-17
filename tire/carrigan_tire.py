from tire.tire import Tire

class CarriganTire(Tire):
  def _init_(self, val):
    self.val = val
  

  def needs_service(self):
    for i in self.val:
      if i >= 0.9:
        return True
        
    return False