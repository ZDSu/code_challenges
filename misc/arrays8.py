# jay's solutions
# given an array of 1 to n-1 with one dup, find the dup

def find_dup(arr, n):
    extraElement = 0
    
    for i in range(0, n):
        element = arr[abs(arr[i])]
        
        if element < 0:
            extraElement = arr[i]
            break
      
        arr[abs(arr[i])] = -arr[abs(arr[i])]
    return abs(extraElement)
      
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
n = len(arr)
find_dup(arr, n)


# find the only  
# repeating element in an array  
# where elements are from 1 to n-1.
def find_dup(arr, n):

    for i in range(0, n):
        element = arr[abs(arr[i])]

        if element < 0:
            return arr[i]

        arr[abs(arr[i])] = -arr[abs(arr[i])]

arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
n = len(arr)
find_dup(arr, n)
# Big O Time: 0(n)  Space 0(1) becuase of jump list