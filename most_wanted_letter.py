'''
    Name     :  Finding most repeated letter in a string
    Author   :  R Gautham Ram
    Tested on:  Python 2.7
    Date created  : 7 Oct 17

'''

import string
def mostwanted(text):
    textTmp = text.replace(" ", "").lower()  #Removes white spaces and makes it lowercase
    maxcount = 0
    a = None
    for item in textTmp:
         if item in string.ascii_letters:    #Allows only ASCII letters
             charcount = textTmp.count(item) 
             if charcount > maxcount:
                maxcount = charcount
                a = item
             elif charcount==maxcount:
                 if item < a :
                     a=item
    return a

if __name__=='__main__':
    print (mostwanted(raw_input("Enter the string:")))

