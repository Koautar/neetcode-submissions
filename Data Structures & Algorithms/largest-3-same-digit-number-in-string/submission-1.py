from collections import Counter 
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = "" 

        for i in range(len(num) - 2):
            bloc = num[i:i + 3] 

            if bloc[0] == bloc[1] == bloc[2]:
                best = max(bloc, best )
        return best 
            



        