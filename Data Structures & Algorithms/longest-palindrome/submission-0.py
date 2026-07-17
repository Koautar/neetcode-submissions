from collections import Counter 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrom = 0
        has_odd = False 
        count = Counter(s)
        for c in count.values(): 
            if c % 2 == 0:
                palindrom += c
            else:
                palindrom += (c - 1)
                has_odd = True
        if has_odd:
                palindrom += 1
        return palindrom 
                
        