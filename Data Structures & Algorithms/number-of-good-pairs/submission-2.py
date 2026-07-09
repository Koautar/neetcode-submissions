

# solution avec hashmap  
from collections import Counter 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:  
        res = 0
        pair = Counter(nums)  
        for value in pair.values():
            res += value * ( value - 1 ) // 2

        return res