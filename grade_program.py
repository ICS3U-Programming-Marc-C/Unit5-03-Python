#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program tells the middle percentage of a grade based on the level


# Defining the function that checks the level and return the middle percentage
def calc_mark(level):
    if level == "4+":
        return "97.5%."
    elif level == "4":
        return "90.5%."
    elif level == "4-":
        return "83%."
    elif level == "3+":
        return "78%."
    elif level == "3":
        return "74%."
    elif level == "3-":
        return "71%."
    elif level == "2+":
        return "68%."
    elif level == "2":
        return "64.5%."
    elif level == "2-":
        return "61%."
    elif level == "1+":
        return "58%."
    elif level == "1":
        return "54.5%."
    elif level == "1-":
        return "51%."
    elif level == "R":
        return "Below 50."
    else:
        return "-1."


if __name__ == "__main__":
    # Getting the height and base from the user
    user_input = input("Enter a level: ")

    # Storing return value inside the percentage variable
    percentage = calc_mark(user_input)

    # Displaying middle percentage to user
    print("The level {} has a middle percentage of {}".format(user_input, percentage))
