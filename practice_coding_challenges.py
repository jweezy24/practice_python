
#reverse a string
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

print(LetterChanges("hello*3"))
