'''
given an unsorted array return if a key 'k' exist. Return if an element exist.
'''
# input: array, k
# output: boolean

# Time complexity of this algorithm is O(n), where n is the size of input array
def linear_search(arr, key):
    for element in arr: #this is same as for each loop in other programming lang
        if(arr[element] == key):
            return True
    return False

# Now, let's say if the interviewer asks you given a sorted array you need to 
# check if an element exist or not?
# whenever you see the word given a "sorted array" the algorithm that comes to 
# our mind is binary search
