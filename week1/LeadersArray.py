class Solution:
    def leaders(self, arr):
        leaders = []
        max_from_right = float('-inf')
        
        # Traverse from right to left
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_from_right:
                leaders.append(arr[i])
                max_from_right = arr[i]
        
        leaders.reverse()
        
        return leaders
