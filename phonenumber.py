import re
phone = input("Please enter your phone number: ")
if not re.match("[\+\d{3}][.-][\d{3}][.-][\d{3}][.-][\d{3}][.-]", phone):
    print("Error! invalid phone")
else:
  print("Your phone number is " + phone)
