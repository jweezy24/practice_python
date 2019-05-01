def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 ==0:
                return True
            else:
                return False
        return True
    return False

while True:
    year = input()
    print(leap_year(int(year)))
