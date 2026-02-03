class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        
        if n < 3:
            return False
        
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):

                if self.isValidSplit(nums, p, q):
                    return True
        
        return False
    
    def isValidSplit(self, nums, p, q):

        for i in range(p):
            if nums[i] >= nums[i + 1]:
                return False
        

        for i in range(p, q):
            if nums[i] <= nums[i + 1]:
                return False
        

        for i in range(q, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True
