class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        length = 0 
        for i in s1:
            length += 1 
            if  i == ' ':
                length = 0 
        return length 
        