from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_magazine = Counter(magazine)
        c_ransomNote = Counter(ransomNote)
        constructed = True
        for c in c_ransomNote:
            if c_ransomNote[c] >  c_magazine[c]: 
                constructed = False 
        return constructed 


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)

        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                magazine.remove(c)

        return True