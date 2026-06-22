from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_odd =  float("-inf")
        max_even = float("-inf")
        for cn in count.values():
            if cn % 2 == 1 :
                max_odd = max(max_odd,cn)
            else:
                max_even = max(max_even,cn)
        return max_odd - max_even 