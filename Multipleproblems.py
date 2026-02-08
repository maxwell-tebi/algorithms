# Multiple problems

class Solution:
    def findSum(self, n):
        sum = 0
        if n == 0:
            sum = 0
            return 0
        else:
            sum = n * (n+1) // 2
            return sum
        
