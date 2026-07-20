class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        exist = set()

        for nbr in nums: 
            if nbr in exist: 
                res.extend([nbr,nbr+1])
            else: 
                exist.add(nbr)
        return res 
        