from collections import Counter 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        count = Counter(words[0])
        for w in words: 
            crnt_word = Counter(w)
            for c in count: 
                count[c] = min(count[c],crnt_word[c])
        
        for c in count: 
            for i in range(count[c]): 
                res.append(c)
        return res 
        