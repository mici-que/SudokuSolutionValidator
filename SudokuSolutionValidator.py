size = 9
root = 3


def validSolution(sudoku=None):
    if not guardian(sudoku):
        return False
    for x in range(size):
        square = {
            sudoku[((x % root) * root) + (y // root)][
                (((x // root) * root) + (y % root))
            ]
            for y in range(size)
        }
        if not (
            len({sudoku[y][x] for y in range(size)})
            == len(set(sudoku[x]))
            == len(square)
            == 9
        ):
            return False
    return True


def guardian(sudoku=None):
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
