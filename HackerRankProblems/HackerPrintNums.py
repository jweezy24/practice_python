def printer(num):
    holder = ''
    for i in range(1,num+1):
        holder += str(i)
    print(holder)

while True:
    num = input()
    printer(int(num))
