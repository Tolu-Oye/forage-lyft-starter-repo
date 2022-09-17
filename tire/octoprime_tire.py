from tire.tire import Tire

class OctoprimeTire(Tire):
  def _init_(self, val):
    self.val = val
  

  def needs_service(self):
    sum = 0
    for i in self.val:
      sum += i
      
    if sum >= 3:
      return True
    
    return False
        