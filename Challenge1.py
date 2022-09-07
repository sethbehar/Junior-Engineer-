# Challenge 1:
'''
Given two sorted arrays (arr1, arr2) and a number, k,
create a method, sortArrays that returns a sorted array
of the first k elements.

Array 1: [1, 3, 5, 8]
Array 2: [1, 2, 3]
Number (k): 5

sortArrays(arr1, arr2, k) returns:
[1, 1, 2, 3, 3]
'''

# combine arrays, sort, and return valid indexes
def sortArrays(a1, a2, num):
     a3 = a1 + a2
     a3.sort()
     return a3[0:num]









