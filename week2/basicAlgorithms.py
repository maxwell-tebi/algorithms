'''
class Solution:
    def search(self, arr, x):
        if x in arr:
            return arr.index(x)
        else:
            return -1
