'''
    Name         :  Caesar algorithm
    Author       :  R Gautham Ram
    Tested on    :  Python 2.7
    Date created :  14 Sep 17
    Description  :  Uses caesar's algorithm for encrypting/decrypting of the string
'''

def caesar_encrypt(a,key):
    str=""
    if key>26:
        key%=26
    for i in range(0,len(a)):
        if a[i].isalpha():
            b=ord(a[i])
            b+=key
            if b>122:
                c=b-122
                str+=chr(96+c)
            else:
                str+=chr(b)
        else:
            str+=a[i]
    print("Encrypted:"+str)


def caesar_decrypt(a,key):
    str=""
    if key>26:
        key%=26
    for i in range(0,len(a)):
        if a[i].isalpha():
            b=ord(a[i])
            b-=key
            if b<65:
                c=b+65
                str+=chr(90-c)
            else:
                str+=chr(b)
        else:
            str+=a[i]
    print("Decrypted:"+str)


choice=int(input('Press 1 for encrypt or 0 for decrypt'))
a=input('Enter the code:')
key=int(input('Enter the key:'))

if choice:
	caesar_encrypt(a,key)
else:
	caesar_decrypt(a,key)
