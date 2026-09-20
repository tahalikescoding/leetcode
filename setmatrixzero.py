#LEETCODE 73: SET MATRIX ZEROES

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        zerorows = set()
        zerocolumns = set()
        for i in range(0,rows):
            for j in range(0,columns):
                if matrix[i][j] == 0:
                    zerorows.add(i)
                    zerocolumns.add(j)

        for i in range(0,rows):
            for j in range(0,columns):
                if i in zerorows or j in zerocolumns:
                    matrix[i][j] = 0 