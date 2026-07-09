
        
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        set_p = set()
        for num in nums: 
            if num not in set_p:
                set_p.add(num)
            else: 
                set_p.remove(num)
        return len(set_p) == 0