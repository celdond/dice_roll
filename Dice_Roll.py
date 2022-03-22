import dice as d

def main():
    dice_set = d.set_dice()
    dice_set.add_dice()
    print("Menu:\nTo roll a die: r\nTo add new dice: a\nTo reset the dice: r\nTo quit: q\n")
    c = input("You start with one die\n")
    while c != "q":
        if c == "r":
            print(dice_set.roll())
        c = input()
main()