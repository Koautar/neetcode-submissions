from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_magazine = Counter(magazine)
        c_ransomNote = Counter(ransomNote)
        constructed = True
        for c in c_ransomNote:
            if c_ransomNote[c] != c_magazine[c]:
                constructed = False 
        return constructed 
