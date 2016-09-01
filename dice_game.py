"""
This is program that rolls 2 die and then the user tries to guess a higher number then the total of the dice roll
"""
# Libraries needed for program to run
from random import randint
from time import sleep


def get_user_guess():
    user_guess = int(raw_input("Guess a number: "))
    return user_guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_value = number_of_sides * 2
    print "The max value that the die can roll is: " + str(max_value)
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_value:
        print "Guess larger than amount on both die!!"
        return
    else:
        print "Rolling.."
        sleep(2)
        print "First roll is: %d" % (first_roll)
        sleep(1)  # Tested code up to this point - Its working
    print "Second roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Calculating results.."
    sleep(1)
    if user_guess > total_roll:
        print "You win! %d is greater than %d" % (user_guess, total_roll)
        return
    else:
        print "I am sorry you lost.. %d is lower than %d" % (user_guess, total_roll)
        return


num_of_sides = int(raw_input("How many side do you want the die to have: "))
roll_dice(num_of_sides)


