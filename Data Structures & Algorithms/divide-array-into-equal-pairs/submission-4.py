from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for value in count.values():
            if value % 2 != 0 :
                return False 
        return True

# solution 2 possible  en utilisant set  
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