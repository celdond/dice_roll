import random

class die:
    
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
        self.rolled = 0

    def load_dice(self, loaded = 0, load = 1):
        if loaded != 0:
            for x in range(load):
                self.sides.append(loaded)
                
    def roll(self):
        x = random.choice(self.sides)
        self.current = int(x)
        return x

class set_dice:

    def __init__(self):
        self.set_of_dice = []
        self.number_of_dice = 0
        self.total = 0

    def create_die(self, loaded = 0, load = 1):
        a = die()
        if loaded != 0:
            a.load_dice(loaded, load)

        self.set_of_dice.append(a)

    def add_dice(self, number = 1, loaded = 0, load = 1):
        self.number_of_dice += number
        for x in range(number):
            self.create_die(loaded, load)

    def roll(self):
        self.total = 0
        for x in range(self.number_of_dice):
            current_dice = self.set_of_dice[x]
            self.total += current_dice.roll()

        return self.total