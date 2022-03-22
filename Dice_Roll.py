import dice as d

def main():
    dice_set = d.set_dice()
    dice_set.add_dice()
    print("Menu:\nTo roll a die: r\nTo add new dice: a\nTo reset the dice: r\nTo quit: q\n")
    c = input("You start with one die\n")
    while c != "q":
        if c == "r":
            print(dice_set.roll())
        elif c == "a":
            dice_set.add_dice(int(input("How many?\n")), int(input("Are they loaded?\n")), int(input("How loaded?\n")))
        c = input()
main()