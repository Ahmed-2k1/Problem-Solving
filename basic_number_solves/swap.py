# swap two numbers
# input:
# Ex: a = 10, b = 20
# Ex: a = 20, b = 10

def swap(a, b):
    temp = a # putting the value of a into temp
    a = b    # putting the value of b into a 
    b = temp # putting the value of temp, which has the value of a, into b
    return a, b

def swap2(a, b): # Another method for swapping 2 numbers
    a, b = b, a  # In this approach the value of a is assigned to b and the value of b is asssigned to a.
    return a, b

