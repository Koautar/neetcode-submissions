"""
LeetCode 2490 - Circular Sentence

Pattern :
- Circular Array
- Modulo (%)

Idée :
- Découper la phrase avec split().
- Comparer la dernière lettre du mot actuel avec la première lettre du mot suivant.
- Utiliser (i + 1) % n pour que le dernier mot revienne au premier.

À retenir :
- Quand il faut comparer le dernier élément avec le premier,
  penser au modulo : (i + 1) % n.
- Le modulo permet de créer une boucle circulaire et d'éviter un IndexError.

Complexité :
Time : O(n)
Space : O(n)
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range (n):
            if words[i][-1] != words[(i+1) % n][0]:
                return False
        return True  
        