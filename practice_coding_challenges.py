
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
