
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        carac_count = defaultdict(int)
        for word in words: 
            #Compter tous les caractères de tous les mots
           for c in word : 
            carac_count[c] += 1

        for c in carac_count:
            #vérifier si chaque fréquence est divisible par le nombre de mots
            if carac_count[c] % len(words) != 0:
                return False 
        return True 

# autre soliution
from collections import Counter   
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter("".join(words))
    
        for nbr in count.values():
            if nbr %  len(words) != 0:
                return False 
        return True 
