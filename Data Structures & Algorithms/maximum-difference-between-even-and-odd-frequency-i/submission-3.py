from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_odd =  float("-inf")
        min_even = float("inf")
        for cn in count.values():
            if cn % 2 == 1 :
                max_odd = max(max_odd,cn)
            else:
                min_even = min(min_even,cn)
        return max_odd - min_even 