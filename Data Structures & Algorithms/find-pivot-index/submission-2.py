class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1 
        left = right = 0
        for i in range(len(nums)):
            right = sum(nums[i+1:])
            left = sum(nums[:i])
            if right == left :
                pivot = i 
        return pivot 
        