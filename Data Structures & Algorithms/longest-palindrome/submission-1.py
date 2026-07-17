"""
Pattern: Counting + Greedy

Idea:
- Count the frequency of each character.
- Use all even frequencies.
- For odd frequencies, use the largest even part (freq - 1).
- If there is at least one odd frequency, place one remaining character
  in the center of the palindrome.

Time: O(n)
Space: O(1)  # O(52) because only English letters (constant space)
"""
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
                
        