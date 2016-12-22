# 21 game
import random

def think(total):
    if total == 18:
        return 3
    if total == 17:
        return 4
    if total == 16:
        return 5
    if total == 15:
        return 6
    if (total - 21) in [2,3,4,5,6,7,8,9]:
        if (total - 21) > 5:
            return 6

while True:

    computer_chance = random.randint(1,3)
    print "My turn: " + str(computer_chance)
    player_chance = int(raw_input("Your turn: "))

    if player_chance > 3 or player_chance<0:
        print "Invalid number!"
        exit()

    total = player_chance + computer_chance

    while True:
        print  "                                Sum=" + str(total)
        print
        c2 = random.randint(1,3)
        think(total)
        print "My turn: " + str(c2)
        total+=c2
        if total == 21:
            break # Computer wins
        else:
            p2 = int(raw_input("Your turn: "))
            if player_chance > 3 or player_chance<0:
                print "Invalid number!"
                exit()

            total+=p2
            if total == 21:
                break

        if total == 21:
            print "You win!"
            break
