size = 9
root = 3


def validSolution(sudoku=None):
    if sudoku == None or not guardian(sudoku):
        return False
    rows = [{0} for x in range(size)]
    cols = [{0} for x in range(size)]
    squares = [{0} for x in range(size)]

    for x in range(size):
        for y in range(size):
            rows[x].add(sudoku[x][y])
            cols[x].add(sudoku[y][x])

            if (x // root == 0) and (y // root == 0):
                squares[0].add(sudoku[x][y])
            if (x // root == 0) and (y // root == 1):
                squares[1].add(sudoku[x][y])
            if (x // root == 0) and (y // root == 2):
                squares[2].add(sudoku[x][y])

            if (x // root == 1) and (y // root == 0):
                squares[3].add(sudoku[x][y])
            if (x // root == 1) and (y // root == 1):
                squares[4].add(sudoku[x][y])
            if (x // root == 1) and (y // root == 2):
                squares[5].add(sudoku[x][y])

            if (x // root == 2) and (y // root == 0):
                squares[6].add(sudoku[x][y])
            if (x // root == 2) and (y // root == 1):
                squares[7].add(sudoku[x][y])
            if (x // root == 2) and (y // root == 2):
                squares[8].add(sudoku[x][y])

    for x in range(size):
        if not (len(rows[x]) == len(cols[x]) == len(squares[x]) == (size + 1)):
            return False
    return True


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


sudokuArray = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
print(validSolution(sudokuArray))
