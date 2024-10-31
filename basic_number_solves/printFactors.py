import math
# Given a number print all of its factors:
# Def: x is said to be a factor of n if it divides n completely
# Ex: 4 is said to be a factor of 24
# Ex: 24: 1,2,3,4,6,8,12,24

#complexity of this approach is O(N)
def printing_factors_Navie(n):
    count = 0
    for element in range(1, n+1): # --------> O(N)
        if n % element == 0:
            count = count + 1
        
    return count
    
# Making it efficient that improving the time complexity:
'''
    6 : 1 2 3 9
    12: 1 2 3 4 6 12
    9 : 1 3 9

    -> we can notice that 1 is always a factor, so reducing one iteration 
    doesn't make much of difference.
    -> we can also notice that all the factors are within N/2, so we 
    need to iterate only till N/2. This is good but not so great improvement.
    -> 
    4 : 1 2 4
    8 : 1 2 4 8
    12: 1 2 3 4 6 12
    16: 1 2 4 8 16 
    
    20:
        2 * 10 = 20
        4 * 5 = 20
        Now, here we can see that 2 is factor in order to get another one we can
        simply do is divide 20/2 which is 10 and hence 10 is also a factor
        so, total factors of 20 are 2, 4, 5, and 10
    -> This algorithm works perfect for all, except for perfect squares.
'''

def is_perfect_square(n):
    sq_root = int(math.sqrt(n))
    return sq_root * sq_root == n


def count_factors_optimised(n):
    count = 0
    sq_root = int(math.sqrt(n))
    upper = sq_root + 1

    for element in range(1, upper):
        if (n % element == 0):
            count = count + 2

    # return count-1 if is_perfect_square(n) else count

    if(is_perfect_square(n)):
        return count - 1
    return count
