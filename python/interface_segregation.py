from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def accelrate(self): ...
    @abstractmethod
    def applyBrakes(self): ...


class Flyable(ABC):
    @abstractmethod
    def fly(self): ...


class Bus(Vehicle):
    def accelrate(self):
        return "accelarate"

    def applyBrakes(self):
        return "apply brakes"


class Aeroplane(Vehicle, Flyable):
    def accelrate(self):
        return "accelrate"

    def applyBrakes(self):
        return "appky brakes"

    def fly(self):
        return "fly"


bus = Bus()
aero = Aeroplane()

print(bus.accelrate())
print(bus.applyBrakes())

print(aero.accelrate())
print(aero.applyBrakes())
print(aero.fly())
