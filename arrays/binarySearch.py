# -> binary search - sorted array, either ascending or descending order.
# -> time complexity is O(log N), where 'N' is the size of the array.
# -> O(log N) because everytime we check the condition that if our 
# mid element is '==' or '>' or '<' key and then we make decision to
# either first half(including mid) or the second half.
# The kth iteration will be N/(2^k)

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == key):
            return True
        elif (key < arr[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False
            