# 1) Find the element that appears once in a sorted array where all other elements appear twice one after another. Find that element in 0(logn) complexity.
# Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}

# Output:  4  

def single_element(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    first = 0
    last = len(arr) - 1

    def binary_search(first, last):
        mid = (first + last) // 2
    
        # even index
        if mid % 2 == 0:
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            elif arr[mid] == arr[mid + 1]:
                first = mid + 1
            else:
                last = mid - 1
        
        #odd index
        else:
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            elif arr[mid] == arr[mid - 1]:
                first = mid - 1
            else:
                last = mid + 1
            