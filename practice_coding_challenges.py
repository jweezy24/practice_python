
#reverse a string
#score 10
def FirstReverse(str):
    # code goes here
    temp = []
    rev = []
    for i in str:
        temp.insert(len(temp), i)
    for i in range(len(temp)-1, -1, -1):
        rev.append(temp[i])
    rev = ''.join(rev)
    return rev

'''Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.  '''
#score 10
def LetterChanges(str):

    # code goes here
    holder = ''
    for i in str:
        if i == 'z':
            i = 'A'
            holder += i
        elif ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i)+1)
            if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
                holder += i.upper()
            else:
                holder += i
        else:
            holder += i
    return holder

'''Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
For the test cases, the parameter num will be any number from 1 to 1000. '''
#score 10
def SimpleAdding(num):

    # code goes here
    temp = 0
    for i in range(0,num+1):
        temp+=i
    return temp

'''Have the function LetterCapitalize(str)
take the str parameter being passed and capitalize the first letter of each word.
Words will be separated by only one space.'''
#score 10
def LetterCapitalize(str):

    # code goes here
    holder = ''
    checker = False
    start = True
    for i in str:
        if checker or start:
            holder += i.upper()
            checker = False
            start = False
            continue
        if i == ' ' and not checker:
            checker = True
            holder += i
            continue
        else:
            holder += i

    return holder


print(LetterCapitalize("i ran there"))
