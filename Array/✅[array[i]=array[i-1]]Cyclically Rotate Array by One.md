### Description: 
- Given an array, rotate the array by one position in clock-wise direction
- https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1



### Example:
#1
- Input: N = 5
- A = {1, 2, 3, 4, 5}
- Output: 5 1 2 3 4

#2
- Input: N = 8
- A = {9, 8, 7, 6, 4, 2, 1, 3}
- Output: 3 9 8 7 6 4 2 1



### Solution:
```
def rotate(arr, n):
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
         
    arr[0] = x
    return arr
    
print(rotate(arr=[9, 8, 7, 6, 4, 2, 1, 3], n=8))
```
