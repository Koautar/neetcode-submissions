from collections import Counter 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        index = -1
        for i , v in enumerate (s):
            if count[v] == 1: 
                index = i
                break 
        return index 
        

        