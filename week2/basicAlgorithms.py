''' 
Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist. 
'''

class Solution:
    def search(self, arr, x):
        if x in arr:
            return arr.index(x)
        else:
            return -1


"To reverse a given string"
class Solution:
     def reverseString(self, s: str) -> str:
        reversed_string = ""
        for i in reversed(s):
            reversed_string += i
            
        return reversed_string
