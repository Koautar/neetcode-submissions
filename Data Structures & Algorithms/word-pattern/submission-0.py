class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False  
        char= {}
        word = {}
        for c,w in zip(pattern,words):
            if c in char:
                if char[c] != w:
                    return False 
            else : 
                char[c] = w
            
            if w in word :
                if word[w] != c:
                    return False 
            else :
                word[w] = c 
        return True  

        