class Solution:
    def check(self, nums: List[int]) -> bool:
        cassure = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]: #  Revenir au début d'un tableau circulaire nums[4] avec nums[0]
                cassure += 1
        
        return cassure <= 1 
     
        