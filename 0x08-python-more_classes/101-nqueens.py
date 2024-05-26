#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
else:
    try:
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)
    except Exception:
        print("N must be a number")
        sys.exit(1)

columns = int(sys.argv[1])
rows = columns
prev_q = [-1, -2]
prev_q_col = []
solutions = []
prev_q_list = []
all_solutions = []
sol = 0
for sol in range(rows - 2):
    column = 0
    while column < columns:
        row = 0
        while row < rows:
            indice = 0
            if (column not in prev_q_col) and ((row != prev_q[1] + 1) and (row != prev_q[1] - 1) and (row != prev_q[1])) and ((row != column) and ([column, row] not in prev_q_list)):
                solutions.append([column, row])
                prev_q[0] = column
                prev_q[1] = row
                prev_q_col.append(column)
                prev_q_list.append([column, row])
                if column < (rows - 1):   
                    column += 1
                    row = 0
                    indice = 1
                else:
                    break
            else:
                row += 1    
        if indice == 0:
            column += 1
    all_solutions.append(solutions.copy())
    solutions.clear()
    prev_q = [-1, -2]
    prev_q_col.clear()
str_solution = str(all_solutions).replace('[[[', ' [[')
str_solution = str_solution.replace(']]]', ']]')
str_solution = str_solution.replace(']],', ']]\n')
print(str_solution)
