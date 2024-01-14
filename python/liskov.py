class Car:
    def wheels(self):
        return "wheels"
    def run(self):
        return "run"

class RealCar(Car):
    def fuel(self):
        return "fuel"

class TeslaToyCar(Car):
    def wheels(self):
        return "tesla toy wheel"

    def run(self):
        return "tesla toy run"

class TeslaRealCar(RealCar):
    def fuel(self):
        return "tesla real fuel"

    def wheels(self):
        return "tesla real wheel"

    def run(self):
        return "tesla real run"

