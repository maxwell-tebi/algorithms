''' 
This is an algorithm challenge from LeetCode.

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''


#The wrong solution I initially thought would work
def solution(nums, target):
  for index1 in nums:
    for index2 in nums:
      if index1 != index2:
        if nums[inidex1] + nums[index2] == target:
          return [index1, index2]

#The final correct solution after several attempts

def solution(nums, target):
  for index1, i in enumerate(nums):
    for index2, j in enumerate(nums):
      if index1 != index2:
        if i + j == target:
          return [index1, index2]
  
