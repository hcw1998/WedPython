# coding: utf-8
def recursive_2(y):
    if(y > 2):
        return recursive_2(y-1)+y
    elif(y == 2):
        return 2
    elif(y == 1):
        return 1
recursive_2(10)
