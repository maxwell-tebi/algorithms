# This is a transformed array problem

def TransformedArray(nums):
  n = len(nums)
  result[0] = [0] * n

  for i in range(n):
    position = (i + nums[i]) % n
    result[i] = nums[position]
    
  return result
