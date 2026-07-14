class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word = sentence.split()
        n = len(word)
        for i in range (n):
            if word[i][-1] != word[(i+1) % n][0]:
                return False
        return True  
        