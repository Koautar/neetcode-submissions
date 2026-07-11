
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        nbr = 0
        
        for word in words: 
            exist = True 
            
            for c in word:
                if c not in allowed: 
                    exist = False 
                    break 
            if exist: 
                nbr += 1
        return nbr 
        

        