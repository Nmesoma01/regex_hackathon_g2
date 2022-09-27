import re
pattern = "^[(^[A-Za-z]+)\s([A-Za-z]+.?)\s([A-Za-z]+)]{1,29}"


full_name = input('Enter your full name: ')

if (re.search(pattern, full_name)):
    print("Valid Name")
else:
    print("Invalid Name")
