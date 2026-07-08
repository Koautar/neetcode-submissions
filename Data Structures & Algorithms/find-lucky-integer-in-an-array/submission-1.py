from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky= -1
        count = Counter(arr)
        for cl,value in count.items():
            if cl == value:
                lucky = max(lucky,value)

        return lucky 

        