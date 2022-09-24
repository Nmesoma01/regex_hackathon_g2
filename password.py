import re
p = re.compile('^(?=.*[!$?])(?=.*[a-z])(?=.*[A-Z]).{8}$')
test_str = 'a2Cd$F!8'
if re.search(p, test_str):
    print('string matched')
