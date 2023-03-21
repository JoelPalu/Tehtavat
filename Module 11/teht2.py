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

class Electric_car(Auto):
    def __init__(self, register, topspeed, W):
        super().__init__(register,topspeed)
        self.wattage = W
        self.wattage_used = 0

    def wattage_calc(self, speed, time):
        self.wattage_used += speed * time / 100 * self.wattage

    def drive(self, time):
        super().travel(time)
        self.wattage_calc(self.speed, time)

class Petrol_car(Auto):
    def __init__(self, register, topspeed, l):
        super().__init__(register,topspeed)
        self.litre = l
        self.litre_used = 0

    def litre_calc(self, speed, time):
        self.litre_used += speed * time / 100 * self.litre


    def drive(self, time):
        super().travel(time)
        self.litre_calc(self.speed, time)


e = Electric_car("ABC-15", 180, 52.5)
p = Petrol_car("ACD-123", 165, 32.3)

e.speed = 150
p.speed = 130

p.drive(3)
e.drive(3)

print(f"Electric car traveled {e.traveled}km and used {e.wattage_used} kW")
print(f"Petrol car traveled {p.traveled}km and used {p.litre_used} l")