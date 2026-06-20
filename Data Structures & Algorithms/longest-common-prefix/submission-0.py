from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # On parcourt les lettres du premier mot
        for i in range(len(strs[0])):

            # La lettre qu'on veut comparer
            char = strs[0][i]

            # On compare cette lettre avec tous les mots
            for word in strs:

                # Si le mot est trop court OU la lettre est différente
                if i >= len(word) or word[i] != char:
                    return prefix

            # Si tous les mots ont la même lettre, on l'ajoute au prefix
            prefix += char

        return prefix