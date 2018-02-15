'''
    Name         :  Password Generator
    Author       :  R Gautham Ram
    Tested on    :  Python 2.7,3.5
    Date created :  23 Sep 17
    Description  :  Generates a random characters of alphanumerals
'''

import random
chars='aABbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
length=int(input('Enter the password length?'))
pw=''
for _ in range(length):
    pw+=random.choice(chars)
print(pw)
