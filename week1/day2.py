#This problem is the Maximum Subarray problem

'''The problem is to find the subarray with the maximum sum for any given array'''

#The first brute force I wrote with time complexity of O(N^2), which was rejected by LeetCode

def MaxSum(nums):
  max_sum = nums[0]
  for start in range(len(nums)):
    running_sum = 0
    for end in range(start, len(nums)):
      running_sum += nums[end]
      if running_sum > max_sum:
        max_sum = running_sum
  return max_sum

#The optimized solution that worked, the Kadane's algorithm

def MaxSum(nums):
  max_sum = nums[0]
  running_sum = 0
  for x in nums:
    running_sum += x
    if running_sum > max_sum:
      max_sum = running_sum
    if running_sum <0:
      running_sum = 0

  return max_sum
