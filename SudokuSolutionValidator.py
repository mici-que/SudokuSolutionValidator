def validSolution(sudoku=None):
    if sudoku == None:
        return False
    if not isinstance(sudoku, list):
        return False
    if len(sudoku) != 9:
        return False
    for row in sudoku:
        if len(row) != 9:
            return False
        for item in row:
            if not isinstance(item, int):
                return False
            if not 0 < item < 10:
                return False
    return True
