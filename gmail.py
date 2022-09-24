#!/usr/bin/env python3
import re
def gmail_checker():
    gmail = input("Enter your gmail: ")
    if not re.match("^[a-z0-9](\.?[a-z0-9]){5,}@gmail\.com$", gmail):
        print("Gmail address does not exist.")
    else:
        print("{} is valid".format(gmail))
