size = 9
root = 3


def addToSet(set, item):
    if item in set:
        return False
    set.add(item)
    return True


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


sudokuArray = [
    [8, 7, 4, 6, 7, 8, 9, 1, 2],
    [6, 3, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
sudokuArray = [[x + 9 * y for x in range(9)] for y in range(9)]
for lines in sudokuArray:
    print((lines))
print(validSolution(sudokuArray))
