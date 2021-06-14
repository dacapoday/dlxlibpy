import dlx

MATRIX_EMPTY = []

MATRIX_WITH_ONE_SOLUTION = [
    [0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1]
]

MATRIX_WITH_THREE_SOLUTIONS = [
    [1, 0, 0, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
]

if __name__ == '__main__':
    print("hello dlxlibpy")
    print(dir(dlx))
    print(dlx.solve(MATRIX_EMPTY))
    print(dlx.solve(MATRIX_WITH_ONE_SOLUTION))
    print(dlx.solve(MATRIX_WITH_THREE_SOLUTIONS))
