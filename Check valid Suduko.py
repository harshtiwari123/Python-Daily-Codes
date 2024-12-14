class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(group):
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for value in group:
                if value == '.':
                    continue
                try:
                    num = int(value)
                    if num in a:
                        a.remove(num)
                    else:
                        return False
                except ValueError:
                    return False
            return True

        for i in range(9):
            if not is_valid_group(board[i]):
                return False

        for j in range(9):
            column_values = [board[i][j] for i in range(9)]
            if not is_valid_group(column_values):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                sub_box = [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]
                if not is_valid_group(sub_box):
                    return False

        return True
