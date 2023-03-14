import random
from time import sleep
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.register = rekisteritunnus
        self.topspeed = huippunopeus
        self.speed = 0
        self.traveled = 0

    def acceleration(self, speed):

        self.speed += speed

        if self.speed >= self.topspeed:
            self.speed = self.topspeed
        elif speed < 0:
            self.speed = 0

    def travel(self, hour):
        self.traveled += self.speed * hour


    pass

cars = []
for n in range(1,11):
    car = Auto("ABC-"+str(n),random.randint(100,200))
    cars.append(car)

while True:
    for car in cars:
        car.acceleration(random.randint(-10,15))
        car.travel(1)
    if car.traveled > 10000:
        break




for car in cars:
    fs = "|{reg:^{w}}|{top:^{w}}|{speed:^{w}}|{traveled:^{w}}|".format(reg = car.register, top = car.topspeed, speed = car.speed, traveled = car.traveled, w = 10)
    print(fs)