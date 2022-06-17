size = 9
root = 3


def validSolution(sudoku=None):
    if sudoku == None or not guardian(sudoku):
        return False


def guardian(sudoku):
    return (
        sudoku != None
        and isinstance(sudoku, list)
        and len(sudoku) == size
        and all(
            [
                True
                if (
                    isinstance(row, list)
                    and (len(row) == size)
                    and all(
                        [
                            True
                            if (isinstance(item, int) and item > 0 and item < size + 1)
                            else False
                            for item in row
                        ]
                    )
                )
                else False
                for row in sudoku
            ]
        )
    )
