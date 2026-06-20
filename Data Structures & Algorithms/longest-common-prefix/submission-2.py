from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # On parcourt les lettres du premier mot bat 
        for i in range(len(strs[0])): # first iteration i = 0 = b 

            # La lettre qu'on veut comparer
            char = strs[0][i] # first iteration i = 0 = b donc char = b 

            # On compare cette lettre avec tous les mots
            for word in strs: 

                # Si le mot est trop court OU la lettre est différente
                # 0 > 3 non et b =! b non 
                if i >= len(word) or word[i] != char:
                    return prefix

            # Si tous les mots ont la même lettre, on l'ajoute au prefix
            prefix += char # prefix = b 

        return prefix