# Check if the given number is prime or not
# prime numbers are used widely used in encryption and decription
import math
def count_factors2(n):
    count = 0
    for element in range(1, n+1): # ----> O(N)
        if(n % element == 0):
            count = count + 1
    return count

def is_prime(n):
    if(count_factors2(n) == 2): # count_factor2(n) ----> O(N)
       return True if count_factors2(n) == 2 else False
    #     return True
    # else:
    #     return False

# time complexity: 
# O(N)
# space complexity:
# O(1), as no extra data structure is used.

'''
Optimised approach for finding if a number is prime or not
'''
# optimised time complexity is O(sqrt(N))
def is_prime_optimised(n):
    upper = math.sqrt(n)
    for element in range(2, upper + 1):
        if(n % element == 0):
            return False
    return True