class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict = {}
        for string in arr:
            dict[string] = dict.get(string,0) + 1
        seen = 0
        for string in arr : 
            if dict[string] == 1:
                seen += 1
                if seen == k:
                    return string 
        return ""