#!/usr/bin/env python3
import re
def dob_checker():
    dob = input("Date of Birth (ddmmyy): ")
    if not re.fullmatch("(0[1-9]|1[0-9]|2[0-9]|3[01])[-/._](0[1-9]|1[012])[-/._]([0-9][0-9])", dob):
        print("Invalid date of birth")
    else:
        print("{} is valid".format(dob))
