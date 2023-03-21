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
        elif self.speed < 0:
            self.speed = 0

    def travel(self, hour):
        self.traveled += self.speed * hour


class Race:

    def __init__(self, name, leinght, cars):
        self.name = name
        self.leinght = leinght
        self.cars = []
        for n in range(1, cars+1):
            car = Auto("ABC-" + str(n), random.randint(100, 200))
            self.cars.append(car)

    def hour_update(self):
        for car in self.cars:
            car.acceleration(random.randint(-10, 15))
            car.travel(1)

    def status(self):
        print(f"|{self.name:^43}|")
        for car in self.cars:
            print(f"|{car.register:^{10}}|{car.topspeed:^{10}}|{car.speed:^{10}}|{car.traveled:^{10}}|")

    def race_over(self):
        for car in self.cars:
            if car.traveled > self.leinght:
                return True
        else:
            return False


race = Race("Suuri romuralli", 8000, 10)
while True:
    if race.race_over() is True:
        print(f"|{'!RACE OVER!':^43}|")
        race.status()
        break
    race.status()
    sleep(1)
    for n in range(10):
        race.hour_update()
        if race.race_over() is True:
            break
