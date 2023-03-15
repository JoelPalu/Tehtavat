from time import sleep
class Hissi:
    def __init__(self,bot,top):
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

H = Hissi(1,20)

while True:
    floor = int(input("To what floor you want to go? 1-20: "))
    H.move_to(floor)