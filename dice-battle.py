#!/usr/bin/env python3

#HH 1200771

# Import needed classes, random to scramble the dice, time to add waiting time when the dice's are rolled.
import random
import sys

# Optional colors to text output.
class BColors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

player_score = 0
computer_score = 0
turn_score = 0


# The main function, does just start the game.
def main():
    while game():
        pass


def game():
    print("I want to play a game called dice-battle. Throw as many time as\n"
          "you like but of you got 1 you lost all you current points.\n")
    while turn():
        pass


def turn():
    global player_score, computer_score, turn_score
    if (player_score) >= 100:
        print(BColors.FAIL+"GAME OVER!"+BColors.ENDC)
        print("Your score: "+str(player_score)+" and my score: "+str(computer_score))
        exit()
    elif (computer_score) >=100:
        print(BColors.FAIL + "GAME OVER!" + BColors.ENDC)
        print("Your score: " + str(player_score) + " and my score: " + str(computer_score))
        exit()
    else:
        print("Your score is: " + str(player_score))
        print("My score is: " + str(computer_score))
        print("\n")
        dice = random.randint(1, 6)
        throw = input("Would you like to throw the dice? y/n: ")
        if throw in ("y", "Y"):
            if dice == 1:
                print(BColors.FAIL+"\nSorry you trew 1. Lost your points and turn.\n"+BColors.ENDC)
                turn_score = 0
                computer_turn()
            else:
                print("You threw: "+str(dice)+"\n")
                turn_score += dice
                print("Current score from this turn is: "+BColors.OKGREEN+str(turn_score)+BColors.ENDC+"\n")
                turn()
        elif throw in ("q"):
            exit()
        elif throw in ("n", "N"):
            player_score += turn_score
            turn_score = 0
            computer_turn()
            print("Now it's my turn!")


def computer_turn():
    global player_score, computer_score, turn_score
    if player_score >= 100:
        turn()
    else:
        dice_probability = []
        dice_throws = random.randint(1, 10)
        while True:
            dice = random.randint(1, 6)
            dice_probability.append(dice)
            if dice == 1:
                print(BColors.FAIL+"\nI lost my points and now it's your turn.\n"+BColors.ENDC)
                turn_score = 0
                turn()
            else:
                turn_score += dice
                print("I threw: "+str(dice))
                if 10 < turn_score < 20 or len(dice_probability) < dice_throws:
                    pass
                else:
                    computer_score += turn_score
                    print("Your turn.")
                    turn_score = 0
                    turn()


# if the program is started straight from the file, then run the game.
if __name__ == "__main__":
    main()
