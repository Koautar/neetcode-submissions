class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subst=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    subst.append(words[i])
                    break # on s'arrete donc on ne check pas le reste des string 
        return subst 

            

        