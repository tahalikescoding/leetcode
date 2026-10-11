#LC 37: SUDOKO SOLVER

class Solution:

    def ss(self,board: list[list[str]] , row , column , rows , cols , boxes) -> bool:
        b = (row//3)*3+column//3

        if row == 9:
            return True
        
        next_row = row
        next_column = column+1
        if column == 8:
            next_row = row + 1
            next_column = 0
        
        if board[row][column] != ".":
            return self.ss(board,next_row,next_column , rows,cols,boxes)
        
        for n in range(1,10):
            if str(n) not in rows[row] and str(n) not in cols[column] and str(n) not in boxes[b]:
                board[row][column] = str(n)
                rows[row].add(str(n))
                cols[column].add(str(n))
                boxes[b].add(str(n))
                if self.ss(board,next_row,next_column , rows, cols, boxes):
                    return True
                board[row][column] = "."
                rows[row].discard(str(n))
                cols[column].discard(str(n))
                boxes[b].discard(str(n))
        return False
        
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                b = (r//3)*3+c//3 
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)
        self.ss(board,0,0,rows,cols,boxes)