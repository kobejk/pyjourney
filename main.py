#!/usr/bin/env python3

from datetime import date, datetime
from simple_term_menu import TerminalMenu
import argparse


def log_message(message):
    today = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")
    file_name = f"{today}.txt"
    with open(file_name, "a") as file:
        file.write(f"[{current_time}] Message: {message}\n")
    print(f"Logged message to '{file_name}'.")


def log_mood(mood):
    today = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")
    file_name = f"{today}.txt"
    with open(file_name, "a") as file:
        file.write(f"[{current_time}] Mood: {mood}\n")
    print(f"Logged mood to '{file_name}'.")


def select_mood():
    options = ["happy", "sad", "anxious", "angry", "annoyed", "excited"]
    terminal_menu = TerminalMenu(
        options, title="How are you feeling today?", accept_keys=("enter", " "))
    menu_entry_index = terminal_menu.show()
    selected_mood = options[menu_entry_index]
    log_mood(selected_mood)


def parse_args():
    parser = argparse.ArgumentParser(
        description='pyjourney :: a python journal.')
    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    # Subparser for logging
    log_parser = subparsers.add_parser('log', help='Log a new message')
    log_parser.add_argument('-m', '--message', type=str,
                            required=True, help='The message to log')

    # Subparser for mood
    subparsers.add_parser('mood', help='Log your current mood')

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()

    if args.command == "log":
        log_message(args.message)
    elif args.command == "mood":
        select_mood()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
