#!/usr/bin/env python3

from datetime import date
import argparse


def log_message(message):
    today = date.today()
    file_name = f"{today}.txt"
    with open(file_name, "a") as file:
        file.write(message + "\n")
    print(f"🤝 Logged to '{file_name}'.")


def log_mood():
    moods = ['happy', 'sad', 'anxious']
    print("How are you feeling? Select a mood:")
    for idx, mood in enumerate(moods, start=1):
        print(f"{idx}. {mood}")

    while True:
        try:
            choice = int(input("Enter the number of your mood: "))
            if 1 <= choice <= len(moods):
                selected_mood = moods[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    log_message(f"Mood: {selected_mood}")


def main():
    parser = argparse.ArgumentParser(description="Journal logging script")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the log command
    log_parser = subparsers.add_parser('log', help='Log a new message')
    log_parser.add_argument('-m', '--message', type=str,
                            required=True, help='The message to log')

    # Subparser for the mood command
    subparsers.add_parser('mood', help='Log your current mood')

    args = parser.parse_args()

    if args.command == "log":
        log_message(args.message)
    elif args.command == "mood":
        log_mood()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
