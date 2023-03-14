class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.register = rekisteritunnus
        self.topspeed = huippunopeus
        self.speed = 0
        self.traveled = 0
    pass

car = Auto("ABC-123", 142)

print(f"Auto {car.register}. Huippunopeus  {car.topspeed}. Auton tämähetkinen nopeus {car.speed} ja matkaa kuljettu {car.traveled}")