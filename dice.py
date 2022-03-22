import random

class die:
    
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
        self.rolled = 0

    def load_dice(self, side = None, load = 1):
        if side != None:
            for x in range(load):
                self.sides.append(side)
                
    def roll(self):
        x = random.choice(self.sides)
        self.current = int(x)
        return x

    def display_die(self):
        top_bdr =  " _______ "
        top =      "|       |"
  
        inside =  ["|       |",\
                   "|   *   |",\
                   "|       |",\

                   "|     * |",\
                   "|       |",\
                   "| *     |",\

                   "| *     |",\
                   "|   *   |",\
                   "|     * |",\

                   "| *   * |",\
                   "|       |",\
                   "| *   * |",\

                   "| *   * |",\
                   "|   *   |",\
                   "| *   * |",\

                   "| *   * |",\
                   "| *   * |",\
                   "| *   * |"]

        bottom =   "|_______|"

        print('{} {}'.format(top_bdr))
        print('{} {}'.format(top))
        for i in range(3):
          pat_1 = (int(self.A.current) - 1) * 3 + (i)
          print('{} {}'.format(inside[pat_1]))
        print('{} {}'.format(bottom))

class set_dice:

    def __init__(self):
        self.set_of_dice = []
        self.number_of_dice = 0
        self.total = 0

    def create_die(self, loaded = None, load = 1):
        a = die
        if loaded != None:
            die.load_dice(loaded, load)

        self.set_of_dice.append(a)

    def add_dice(self, number = 1, loaded = None, load = 1):
        self.number_of_dice += number
        for x in range(number):
            self.create_die(loaded, load)

    def roll(self):
        self.total = 0
        for x in range(self.number_of_dice):
            self.total += self.set_of_dice[x].roll()

        return self.total