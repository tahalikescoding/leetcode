#LEETCODE 36: VALID SUDOKO 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == ".":
                    continue
                b = (row//3)*3 + column//3
                if num in rows[row] or num in columns[column] or num in boxes[b]:
                    return False
                rows[row].add(num)
                columns[column].add(num)
                boxes[b].add(num)
        return True