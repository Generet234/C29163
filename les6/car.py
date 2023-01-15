class OutOfFuel(Exception):
    def __init__(self,message="Not enough fuel to continue driving"):
        Exception.__init__(self,message)

class Car:
    consufuel = 0.1
    fuel = 0
    traveled = 0

    def __init__(self, fuel=0, consufuel=0.1):
        self.fuel = max(fuel, 0)
        self.consufuel = consufuel
        self.traveled = 0

    def go(self,distance):
        fuel_need = distance * self.consufuel
        if self.fuel >= fuel_need:
            self.traveled += distance * self.consufuel
            self.fuel -= fuel_need
        else:
            self.consufuel = fuel_need/distance
            raise OutOfFuel()
