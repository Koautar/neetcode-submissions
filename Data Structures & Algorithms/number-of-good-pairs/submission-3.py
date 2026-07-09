
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums)): 
                # for j in range(i+1,len(nums)) sans i<j
                if i < j and nums[i] == nums[j]:
                    good += 1
        return good 

# solution avec hashmap  
from collections import Counter 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:  
        res = 0
        pair = Counter(nums)  
        for value in pair.values():
            res += value * ( value - 1 ) // 2

        return res