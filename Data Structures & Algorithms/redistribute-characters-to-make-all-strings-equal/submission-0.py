class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        carac_count = defaultdict(int)
        for word in words: 
           for c in word : 
            carac_count[c] += 1

        for c in carac_count:
            if carac_count[c] % len(words) != 0:
                return False 
        return True 


        