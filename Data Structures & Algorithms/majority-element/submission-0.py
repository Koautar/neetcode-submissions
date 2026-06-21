class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0)+1
            if dict[num] > len(nums) // 2:
                return num
        