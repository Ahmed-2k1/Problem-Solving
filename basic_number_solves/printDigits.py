# Given a number print the digits:
# Ex: "123" -> 1 2 3

def print_numbers(n):
    while(n > 0):
        rem = n % 10
        n = n // 10
        print(rem)

# Also write a function to added the digits of the number
def print_numbers_sum(n):
    sum = 0
    while (n > 0):
        rem = n % 10
        n = n // 10
        sum = sum + rem
    return sum

# Print the digits in correct order:
# Since we extracting the digits in the reverse order, now we are seeing how can we print it in the correct order.

def print_in_correct_order(n):
    digits = []

    while (n > 0):
        rem = n % 10
        n = n // 10
        digits.append(rem)
    
    digits.reverse()
    for elements in digits:
       print(elements)
    
    