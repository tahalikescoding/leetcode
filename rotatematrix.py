#LEETCODE 48: ROTATE IMAGE BY 90 

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(0,rows):
            for j in range(i+1,columns):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] 
        
        for row in matrix:
            row.reverse()
