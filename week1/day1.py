#The wrong solution and what I thought would work
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
  
