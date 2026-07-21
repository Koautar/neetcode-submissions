class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set() 
        nums2 = set(nums2)
        for nbr in nums1: 
            for nbr2 in nums2: 
                if nbr == nbr2:
                    res.add(nbr)
        return list(res)
