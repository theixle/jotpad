#!/usr/bin/env python3

import sys

class JournalApp:
    def __init__(self):
        self.user_input = ""
        self.file_path = "journal_entries.txt"

    def say_hello(self):
        print("Hello and welcome to your journal app.")
        print("To store a new entry, just type it at the prompt below.")
        print("To execute a command, start your input with a period. Ex: .? for all commands")

# working here
    def show_commands(self):
        print("Here are the available commands:")
        print(".?", "\t", ": show available commands")
        print(".exit", "\t", ": exit the app")

    def get_input(self):
        self.user_input = input("[Prompt] ")
        return self.user_input

    def execute_command(self, command):
        if command == ".exit":
            exit_conf = input("You want to exit, is that correct? Exit? [y]/n : ")
            if exit_conf.lower() == "y" or exit_conf == "":
                self.save_entries()
                sys.exit()
        elif command == ".?":
            self.show_commands()
        else:
            print("Unknown command. Type '.exit' to exit.")

    def add_input(self, user_input):
        print(f"Adding entry: {user_input}")
        with open(self.file_path, "a") as file:
            file.write(user_input + "\n")

    def read_entries(self):
        try:
            with open(self.file_path, "r") as file:
                entries = file.readlines()
                print("Previous entries:")
                print("".join(entries))
        except FileNotFoundError:
            print("No previous entries found.")

    def save_entries(self):
        print("Saving entries to file.")

    def evaluate_input(self, user_input):
        if user_input.startswith("."):
            self.execute_command(user_input)
        else:
            self.add_input(user_input)

    def loop_prompt(self):
        self.read_entries()
        while True:
            user_input = self.get_input()
            self.evaluate_input(user_input)

if __name__ == "__main__":
    journal_app = JournalApp()
    journal_app.say_hello()
    journal_app.loop_prompt()
