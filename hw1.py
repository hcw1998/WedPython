# coding: utf-8
def recursive(x):
    if(x > 1):
        return recursive(x-1)*x
    else:
        return 1 
recursive(5)
