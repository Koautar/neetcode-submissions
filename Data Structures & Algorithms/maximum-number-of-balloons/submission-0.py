from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
    
        for c in balloon: 
            res = min(res,count_text[c]// balloon[c])
        return res 

        