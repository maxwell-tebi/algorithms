# Mission in array problem

def Solution(nums):
  sum1 = sum(nums)
  n = len(nums) + 1
  sum2 = n * (n +1) // 2

  return sum2 - sum1
