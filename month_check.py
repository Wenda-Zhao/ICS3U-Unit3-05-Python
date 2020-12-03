#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program check the month


import random


def main():
    # this function is check the month

    # input
    month = int(input("Enter the month: "))
    print("")

    # process
    if month == 1:
        # output
        print(" January ")
    # process
    elif month == 2:
        # output
        print(" February ")
    # process
    elif month == 3:
        # output
        print(" March ")
    # process
    elif month == 4:
        # output
        print(" April ")
    # process
    elif month == 5:
        # output
        print(" May ")
    # process
    elif month == 6:
        # output
        print(" June ")
    # process
    elif month == 7:
        # output
        print(" July ")
    # process
    elif month == 8:
        # output
        print(" August ")
    # process
    elif month == 9:
        # output
        print(" September ")
    # process
    elif month == 10:
        # output
        print(" October ")
    # process
    elif month == 11:
        # output
        print(" November ")
    # process
    elif month == 12:
        # output
        print(" December ")
    # process
    else:
        # output
        print(" Sorry, it's not a month! ")

    print("")
    print(" Done!")


if __name__ == "__main__":
    main()
