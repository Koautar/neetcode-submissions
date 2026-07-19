class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        longest = -1
        for position ,  char in enumerate(s):
            if char in first : 
                distance = position - first[char] - 1
                longest = max (longest , distance)
            else: 
                first[char] = position 
        return longest




         


