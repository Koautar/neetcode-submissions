from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = 1
        croi = 1
        desc = 1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                desc += 1
                croi = 1

            elif nums[i] < nums[i + 1]:
                croi += 1
                desc = 1

            else:
                croi = 1
                desc = 1

            best = max(best, croi, desc)

        return best