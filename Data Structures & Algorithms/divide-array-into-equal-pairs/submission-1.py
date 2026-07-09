from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for value in count.values():
            if value % 2 != 0 :
                return False 
        return True
        