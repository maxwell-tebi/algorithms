#Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.
class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        # Euclidean algorithm for GCD
        Big = max(a, b)
        Small = min(a, b)
        
        while Small != 0:
            Big, Small = Small, Big % Small
        
        GCD = Big  # GCD is the last non-zero value
        LCM = abs(a * b) // GCD  # Use integer division
        
        return [LCM, GCD]

#Other optimized approaches
from math import gcd, lcm

class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        return [lcm(a, b), gcd(a, b)]

#Given a positive integer, n. Find the factorial of n.
    # Function to calculate factorial of a number.
def factorial(self, n: int) -> int:
        
    fact = 1
        
    for i in range(1, n+1):
        fact *= i
            
        return fact
