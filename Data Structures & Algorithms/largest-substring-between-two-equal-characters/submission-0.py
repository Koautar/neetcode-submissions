class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        best = -1
        for i in range(len(s)) :
            for j in range(i+1 ,len(s)):
                if s[i] == s[j]:
                    best = max( best , j - i - 1)
        return best 


