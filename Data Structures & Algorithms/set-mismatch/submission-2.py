class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0,0]

        for i  in range(1,n+1) : 
            count = 0
            for  nbr  in nums: 
                if nbr == i : 
                    count+=1
            if count == 2:
                res[0] = i 
            elif count == 0:
                res[1] = i 
        return res 



                
        
        