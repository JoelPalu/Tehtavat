from time import sleep
class Hissi:
    def __init__(self,id, bot, top):
        self.id = id
        self.bot = bot
        self.top = top
        self.floor = bot

    def floor_down(self):
        self.floor -= 1

        if self.floor <= self.bot:
            self.floor = self.bot
        print(self.floor)
        sleep(0.5)

    def floor_up(self):
        self.floor += 1

        if self.floor >= self.top:
            self.floor = self.top

        print(self.floor)
        sleep(0.5)

    def move_to(self, floor):

        while self.floor != floor and self.top >= floor and self.bot <= floor:
            if self.floor < floor:
                self.floor_up()
            elif self.floor > floor:
                self.floor_down()

class House:
    def __init__(self, hissi, bot, top):
        self.hissit = hissi
        self.topfloor = top
        self.botfloor = bot
        self.elevators = []
        for n in range(hissi):
            self.elevators.append(Hissi(n, bot, top))

    def move_elevator(self, hissi, floor):
        self.elevators[hissi-1].move_to(floor)


home = House(3,1,20)

while True:
    print(f"There is {len(home.elevators)} elevators. There is {home.topfloor} floors.")

    elevator, floor = int(input("Which elevator you like to use?: ")), int(input(f"To what floor you want to go? {home.botfloor}-{home.topfloor}: "))
    home.move_elevator(elevator, floor)