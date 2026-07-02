class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                res += nums[i]
            else:
                res = nums[i]
            best = max(res,best)         
        return best 
