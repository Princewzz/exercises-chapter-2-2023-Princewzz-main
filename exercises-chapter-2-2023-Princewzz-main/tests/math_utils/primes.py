from math import *

def isprime(n):
    flag = False
    if n == 1 or n == 4:
        return False 
    if n == 2 or n == 3:
        return True 
    elif n > 4:
        for i in range(2, int(sqrt(n))):
            if (n % i) == 0:
                flag = True
                break 

        if flag:
            return False
        else:
            return True


        

