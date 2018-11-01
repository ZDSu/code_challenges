# given an array of 1 to n-1 with one dup, find the dup

def find_dup(arr, n):
    extraElement = 0
    
    for i in range(0, n):
        element = arr[abs(arr[i])]
        
        if element < 0:
            extraElement = arr[i]
            break
      
        arr[abs(arr[i])] =- arr[abs(arr[i])]
    return abs(extraElement)
      
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
n = len(arr)
find_dup(arr, n)