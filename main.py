#!/usr/bin/env python3

from datetime import date

today = date.today()
file_name = f"{today}.txt"

log_input = input("What's on your mind?: ")

file = open(file_name, "a")
file.write(log_input + "\n")
file.close()
