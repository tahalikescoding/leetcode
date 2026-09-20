#LEETCODE 1579: DIAGONAL MATRIX SUM 

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total = 0
        rows = len(mat)
        columns = len(mat[0])
        rnum = 0
        colnum = columns-1
        while colnum>=0:
            if rnum != colnum:
                total+= mat[rnum][colnum]
            rnum+=1
            colnum-=1
        rnum = colnum = 0 
        while rnum<rows:
            total+= mat[rnum][colnum]
            rnum+=1
            colnum+=1

        return total
        