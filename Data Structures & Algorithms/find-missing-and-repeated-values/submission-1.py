from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {} # i can use defaultdict(int) also 

        for row in grid:
            for val in row:
                count[val] = count.get(val, 0) + 1

        repeated = -1
        missing = -1

        for x in range(1, n * n + 1):
            if count.get(x, 0) == 2:
                repeated = x
            elif count.get(x, 0) == 0:
                missing = x

        return [repeated, missing]
 