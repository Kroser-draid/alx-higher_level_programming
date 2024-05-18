#!/user/bin/python3
import sys
if len(sys.argv) > 2 or len(sys.argv) == 1:
    print("Usage: nqueens N")
    exit(1)
else:
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if arg < 4:
        print("N must be at least 4")
        exit(1)
    else:
        #solutions = []
        solution = []
        prev = 0
        prev_i = -1
        for i in range(arg):
            for j in range(arg):
                if (j != i) and (j != prev + 1) and (j != prev - 1) and (i != prev_i) and (j not in solution):
                    solution.append((i, j))
                    prev = j
                    prev_i = i
        print(solution)