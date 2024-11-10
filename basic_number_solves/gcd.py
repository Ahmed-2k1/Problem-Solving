# Given two numbers calculate GCD:

'''
no need of (a < b) and then swapping it because a % b when a < b is a itself
and in the next iteration the numbers are apperantly swapped.
'''
def gcd(a, b):
    if(a < b):
        a, b = b, a
    
    while(b > 0):
        rem = a % b
        a = b
        b = rem
    
    return a    

'''
If i wanted to calculate lcm the formula we can use is
lcm = (a * b)/gcd
'''