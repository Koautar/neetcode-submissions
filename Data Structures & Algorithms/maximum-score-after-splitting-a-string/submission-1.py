class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]

            zero = left.count("0")
            ones = right.count("1")

            somme = zero + ones 

            res = max(res,somme)
        return res 
        

            
        