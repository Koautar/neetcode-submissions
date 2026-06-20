class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        rest = 0
        for i in nums:
            if i == 1:
                counter += 1 
                rest= max(rest,counter)
            else:
                 counter = 0 
        return rest 

        