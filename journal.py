#!/usr/bin/env python3

# Import required modules
import sys

# Define purpose
'''
  A simple app to practice Python with. It will let me store notes and
  eventually help me retrieve/search those notes.
'''

# Define globals
user_input = ""

# Define functions
def say_hello():
    print("Hello and welcome to your journal app.")
    print("To store a new entry just type it at the prompt below.")
    print("To execute a command, start your input with a period.")

def get_input():
    user_input = input("[Prompt] ")
    return user_input

def evaluate_input(some_input):
    if some_input[0] == ".":
        # do the command things
        print("You tried to use a command.")
    else:
        # do the regular input things
        print("You tried to add input.")

    if some_input == ".exit":
        print("You want to exit, is that correct?")
        exit_conf = input("Exit? [y]/n : ")
        if exit_conf.lower() == "y":
            sys.exit()

def loop_prompt():
    while True:
        evaluate_input(get_input())

# Main execution
if __name__ == "__main__":
    say_hello()
    loop_prompt()
    