import random
chars='aABbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
length=int(input('password length?'))
pw=' '
for _ in range(length):
    pw+=random.choice(chars)
print(pw)
