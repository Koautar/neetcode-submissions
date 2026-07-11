from  collections import Counter 
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_count = Counter(chars)
        for word in words: 
            word_count = Counter(word)
            match = True  
            for  c in word_count :
                if word_count [c] > char_count[c]:
                    match = False 
                    break
            if match: 
                res += len(word)
        return res 

            

        