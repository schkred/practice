from datetime import datetime as dt

class Car(object):
    def __init__(self, model, year, color):
        self.vendor, self.model = model.split(' ', 1)
        self.color = color
        self.year = year
    
    @property
    def age(self):
        return dt.now().year - self.year
        
car = Car('BMW x5', 2010, 'Black')
print car.year
print car.age