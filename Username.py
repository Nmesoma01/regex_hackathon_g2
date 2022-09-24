import re
Username = input("Please enter your username: ")
if not re.match("(^[A-Z]([a-z]*[A-Z])[a-z]*$)", Username):
    print("Misprint! invalid Username")
else:
    print("Your user name is " + Username)
