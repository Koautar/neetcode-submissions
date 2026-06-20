class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            ligne = [1] * ( i + 1 )
            for j in range (1,i):
                ligne[j] = triangle[i-1][j] + triangle[i-1][j-1]
            triangle.append(ligne)
        return triangle 

        