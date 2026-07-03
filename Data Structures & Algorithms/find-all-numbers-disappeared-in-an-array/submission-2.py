class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for nbr in range(1,n+1): # on veux parcourir tt les nbre entre 1 et n 
            if nbr not in nums:
                res.append(nbr)
        return res 



        