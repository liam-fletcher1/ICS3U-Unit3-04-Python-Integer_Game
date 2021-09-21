#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to input a integer and the program tell them if the integer is positive, negative or zero

import random


def main():
    # this tells the user if they picked a positive, negative or zero

    # input
    integer_input = int(input("Enter an integer: "))

    # process & output
    if integer_input > 0:
        print("This is a positive number!")
    elif integer_input < 0:
        print("This is a negative number!")
    elif integer_input == 0:
        print("This is just the number zero!")
    else:
        print("No idea!")
    print("\nDone.")


if __name__ == "__main__":
    main()
