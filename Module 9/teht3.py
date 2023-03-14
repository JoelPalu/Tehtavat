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

car = Auto("ABC-123", 142)

car.acceleration(30)
car.travel(1)
car.acceleration(70)
car.travel(2.1)
car.acceleration(50)
car.travel(1.3)
print(car.speed)
print(car.traveled)
car.acceleration(-200)
print(car.speed)
print(car.traveled)

