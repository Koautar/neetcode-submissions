class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for i , j in zip(heights,expected):
            if i !=j : 
                count += 1
        return count
        