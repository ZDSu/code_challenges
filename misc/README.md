(array challenges from jay adams's DS&A course)

1)Find the element that appears once in a sorted array where all other elements appear twice one after another. Find that element in 0(logn) complexity.  
Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}  
Output:  4

2)A magic index in an array A[0…n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index if one exists, in an array A. FOLLOW UP: What if the values are not distinct?  
Magic index is given a sorted array of distinct numbers find the index that matches the element value.

3)Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.  
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] key = 6  
output is 2  

Search an element in sorted and rotated array using single pass of binary Search.

Returns index of key in arr[start...end] if key is present,
otherwise returns -1

4)Given an array that contains numbers from 1 to n-1 and exactly 1 duplicate, find that duplicate.

5)Search an element in an array where difference between adjacent elements is 1.
For example: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}

Search for 3 and Output: Found at index 7

6)Given an array of numbers, split the array into two where one array contains the sum of n-1 numbers and the other array with all the n-1 elements. (edited)

That will cover arrays (first week)

Questions from second round

6)Given a sorted array, use binary search to return the one element that isnt duplicated; time complexity is 0(logn)  
(ex: `arr = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]` returns 4)

7)Given a sorted array that has been pivoted n times, find the index of target using binary search; time complexity is 0(logn)   
(ex: `arr = [9, 10, 11, 12, 1, 2, 4, 5]`, `target = 2`)

8)Given an array of 1 to n-1 with one dup, find the dup  
(ex: `arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]`, `n = len(arr)` )

9)Search for an element in an array where the differnce between all adjacent ellements is 1  
arr = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]  
n = len(arr)  
target = 3  
So, given an array where the difference between adjacent elements is 1, find the index for the first occurrence of the target element (ex: [8,7,6,7,6,5,4,3,4,3,2], target = 3)

10)Given an array of numbers, split the array into two where one array contains the sum of n-1 numbers and the other array with all the n-1 elements.  
(ex: `arr = [1,2,3,5,28]` and `n = len(arr)` returns `[1, 2, 3]` and `[6]`