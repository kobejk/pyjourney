#!/usr/bin/env python3

from datetime import date, datetime
from simple_term_menu import TerminalMenu
import argparse


def get_date():
    return date.today()


def get_time():
    return datetime.now().strftime("%H:%M:%S")


def get_filename():
    return f"{get_date()}.md"


def log_message(message):
    with open(get_filename(), "a") as file:
        file.write(f"[{get_time()}] Message: {message}\n")
    print(f"Logged message to '{get_filename()}'.")


def log_mood(mood):
    with open(get_filename(), "a") as file:
        file.write(f"[{get_time()}] Mood: {mood}\n")
    print(f"Logged mood to '{get_filename()}'.")


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
    elif args.command == "todo":
        log_todo()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
