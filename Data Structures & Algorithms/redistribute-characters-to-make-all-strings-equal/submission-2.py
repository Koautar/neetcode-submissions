


# autre soliution
from collections import Counter   
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter("".join(words))
    
        for nbr in count.values():
            if nbr %  len(words) != 0:
                return False 
        return True 
