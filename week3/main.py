#Min and Max in an array using basic min and max methods.
class Solution:
    def getMinMax(self, arr):
        return [min(arr),max(arr)]
      

#Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.
class Solution:
   
    def searchInSorted(self,arr, k):
        
        if k in arr:
            return True
        else:
            return False

#You are given an integer n. You have  to print all numbers from 1 to n. Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.
class Solution: 
    def printNos(self,n):
        if n>0:
            self.printNos(n-1)
            print(n, end=" ")
#
