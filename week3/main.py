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
#Given a number n, return an array containing the first n Fibonacci numbers. Note: The first two numbers of the series are 0 and 1.
class Solution:
    def fibonacciNumbers(self,n):
        sequence = [0,1]
        
        if n == 1:
            sequence = [0]
        elif n != 2:
            while len(sequence)<n:
                sequence.append(sequence[-1]+sequence[-2])
                
        
        return sequence

#Given an array arr[]. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ). Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.
class Solution:
    def valueEqualToIndex(self, arr):
        answer = []
        for i, j in enumerate(arr, start=1):
            if i == j:
                answer.append(i)
        return answer
