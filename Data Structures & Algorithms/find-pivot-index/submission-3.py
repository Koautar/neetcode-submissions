class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = right = 0
        for i in range(len(nums)):
            right = sum(nums[i+1:])
            left = sum(nums[:i])
            if right == left :
                return i 
        return -1 
        