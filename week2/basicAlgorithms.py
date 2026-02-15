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


#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count_a = Counter(a)
        for x in b:
            if count_a[x] == 0:
                return False
            count_a[x] -= 1
        
        return True
    
    
    
#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
class Solution:
    from collections import Counter
    def getSecondLargest(self, arr):
        
        sorted_arr = sorted(arr, reverse=True)
        
        maximum = max(sorted_arr)
        
        
        for i in sorted_arr:
            
            if i<maximum:

                return i
                
                break
            
        return -1
