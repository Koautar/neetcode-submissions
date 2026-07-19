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

# solution 2
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        best = -1
        for i in range(len(s)) :
            for j in range(i+1 ,len(s)):
                if s[i] == s[j]:
                    best = max( best , j - i - 1)
        return best


         


