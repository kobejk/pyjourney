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


def log_todo(todo):
    with open(get_filename(), "a") as file:
        file.write(f"[{get_time()}] Todo: [ ] {todo}\n")
    print(f"Logged todo to '{get_filename()}'.")


def complete_todo():
    try:
        with open(get_filename(), "r") as file:
            lines = file.readlines()
        todos = [line for line in lines if "[ ]" in line]
        if not todos:
            print("No todos for today.")
            return

        terminal_menu = TerminalMenu(
            todos, title="Which todos have you completed?", multi_select=True, show_multi_select_hint=True, accept_keys=("enter", " "))
        menu_entry_indices = terminal_menu.show()
        selected_todos = [todos[i] for i in menu_entry_indices]

        with open(get_filename(), "w") as file:
            for line in lines:
                if line in selected_todos:
                    file.write(line.replace("[ ]", "[x]"))
                else:
                    file.write(line)
        for todo in selected_todos:
            print(f"Checked off todo: '{todo.strip()}'.")
    except FileNotFoundError:
        print("No log file has been created for today.")


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

    # Subparser for logging
    todo_parser = subparsers.add_parser('todo', help='Add a todo to your list')
    todo_parser.add_argument('-a', '--add', type=str,
                             required=False, help='The todo to add')
    todo_parser.add_argument('-c', '--check', action='store_true',
                             help='Check off a completed todo')

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()

    if args.command == "log":
        log_message(args.message)
    elif args.command == "mood":
        select_mood()
    elif args.command == "todo":
        if args.add:
            log_todo(args.add)
        elif args.check:
            complete_todo()
        else:
            parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
