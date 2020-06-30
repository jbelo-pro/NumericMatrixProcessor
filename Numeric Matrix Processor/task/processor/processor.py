from collections import deque

def sum_matrices():
    rows_1, col_1 = input('Enter size of first matrix: ').split()
    print('Enter first matrix:')
    matrix_1 = []
    for r in range(int(rows_1)):
        row = []
        for n in input().split():
            t = int(n) if n.isdigit() else float(n)
            row.append(t)
        matrix_1.append(row)

    rows_2, col_2 = input('Enter size of second matrix: ').split()
    print('Enter second matrix:')
    matrix_2 = []
    for r in range(int(rows_2)):
        row = []
        for n in input().split():
            t = int(n) if n.isdigit() else float(n)
            row.append(t)
        matrix_2.append(row)

    if rows_1 != rows_2 or col_1 != col_2:
        print('The operation can not be performed\n')
    else:
        sum_matrix = []
        print('The result is:')
        for r in range(len(matrix_1)):
            temp_r = []
            for z in zip(matrix_1[r], matrix_2[r]):
                temp_r.append(str(z[0] + z[1]))
            print(' '.join(temp_r))
        print('\n')


def matrix_by_constant(cons, matrix):
    new_matrix = []
    for row in matrix:
        temp_r = [n * cons if abs(n) != 0 else 0 for n in row]
        new_matrix.append(temp_r)
    return new_matrix


def multiply_matrices():

    rows_1, col_1 = input('Enter size of first matrix: ').split()
    print('Enter first matrix:')
    matrix_1 = []
    for r in range(int(rows_1)):
        row = []
        for n in input().split():
            t = int(n) if n.isdigit() else float(n)
            row.append(t)
        matrix_1.append(row)

    rows_2, col_2 = input('Enter size of second matrix: ').split()
    print('Enter second matrix:')
    matrix_2 = []
    for r in range(int(rows_2)):
        row = []
        for n in input().split():
            t = int(n) if n.isdigit() else float(n)
            row.append(t)
        matrix_2.append(row)

    if col_1 != rows_2:
        print('The operation can not be performed\n')
    else:
        t_matrix_2 = []
        for r in range(int(col_2)):
            t_matrix_2.append([])

        for r in matrix_2:
            for c in range(len(r)):
                t_matrix_2[c].append(r[c])

        new_matrix = []

        for r in matrix_1:
            new_row = []
            for r1 in t_matrix_2:
                value = 0
                for z in zip(r, r1):
                    value += z[0] * z[1]
                new_row.append(str(value))

            new_matrix.append(new_row)

        print('The result is:')
        for r in new_matrix:
            print(' '.join(r))
        print('\n')


def transpose_main_diagonal(matrix):
    t_matrix = []
    for r in range(len(matrix[0])):
        t_matrix.append([])

    for r in matrix:
        for c in range(len(r)):
            t_matrix[c].append(r[c])
    return t_matrix


def transpose_side_diagonal():

    rows, cols = input('Enter matrix size: ').split()
    print('Enter matrix')
    matrix = []
    for r in range(int(rows)):
        row = [n for n in input().split()]
        matrix.append(row)

    t_matrix = []
    for r in range(len(matrix[0])):
        t_matrix.append([])

    for r in matrix:
        for c in range(len(r)):
            t_matrix[c].append(str(r[c]))

    t_matrix.reverse()
    for r in t_matrix:
        r.reverse()
        print(' '.join(r))


def transpose_vertical_line():
    rows, cols = input('Enter matrix size: ').split()
    print('Enter matrix')
    matrix = []
    for r in range(int(rows)):
        row = [n for n in input().split()]
        matrix.append(row)

    for r in matrix:
        r.reverse()
        print(' '.join(r))


def transpose_horizontal():
    rows, cols = input('Enter matrix size: ').split()
    print('Enter matrix')
    matrix = []

    for r in range(int(rows)):
        row = [n for n in input().split()]
        matrix.append(row)
    matrix.reverse()

    for r in matrix:
        print(' '.join(r))


def determinant(mtrx):
    if len(mtrx) == 2:
        return mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
    elif len(mtrx) == 1:
        return mtrx[0][0]
    else:
        deter = 0
        for index in range(len(mtrx[0])):
            cof = mtrx[0][index]
            sym = (-1) ** (1 + index + 1)
            new_matrix = []
            for row_index in range(1, len(mtrx)):
                row = mtrx[row_index]
                nr = []
                for index2 in range(len(mtrx[0])):
                    if index2 == index:
                        continue
                    nr.append(row[index2])
                new_matrix.append(nr)
            deter += cof * sym * determinant(new_matrix) # (new_matrix[0][0] * new_matrix[1][1] - new_matrix[0][1] * new_matrix[1][0])
        return deter


def get_matrix():
    rows, cols = input('Enter matrix size: ').split()
    print('Enter matrix')
    matrix = []
    for r in range(int(rows)):
        row = [int(n) if n.isdigit() else float(n) for n in input().split()]
        matrix.append(row)
    return matrix


def sub_matrix(row, column, matrix):
    new_matrix = []
    for row_index in range(len(matrix)):
        if row_index == row:
            continue
        new_row = []
        row_m = matrix[row_index]
        for column_index in range(len(row_m)):
            if column_index == column:
                continue
            new_row.append(row_m[column_index])
        new_matrix.append(new_row)
    return new_matrix


def attached_matrix(matrix):
    new_matrix = []
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        new_row = []
        for column_index in range(len(row)):
            c = (-1) ** (row_index + column_index + 2) * determinant(
                sub_matrix(row_index, column_index, matrix))
            new_row.append(c)
        new_matrix.append(new_row)

    return new_matrix


def print_options():
    print('1. Add matrices')
    print('2. Multiply matrix by constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')


def print_options_transpose():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')


while True:
    print_options()
    choice = input('Your choice : ')
    if choice == '1':
        sum_matrices()
    elif choice == '2':
        matrix = get_matrix()
        cons = input('Enter constant: ')
        cons = int(cons) if cons.isdigit() else float(cons)
        matrix_by = matrix_by_constant(cons, matrix)
        print('The result is:')
        for row in matrix_by:
            print(' '.join([str(n) for n in row]))
        print('\n')
    elif choice == '3':
        multiply_matrices()
    elif choice == '4':
        print_options_transpose()
        choice_transponse = input('Your choice: ')
        if choice_transponse == '1':
            matrix = get_matrix()
            t_matrix = transpose_main_diagonal(matrix)
            for row in t_matrix:
                print(' '.join([str(n) for n in row]))
        elif choice_transponse == '2':
            transpose_side_diagonal()
        elif choice_transponse == '3':
            transpose_vertical_line()
        else:
            transpose_horizontal()
    elif choice == '5':
        matrix = get_matrix()
        d = determinant(matrix)
        print('The result is:')
        if d % 1 > 0:
            print(d, '\n')
        else:
            print(int(d), '\n')

    elif choice == '6':
        matrix = get_matrix()
        matrix_determinant = determinant(matrix)
        if matrix_determinant == 0:
            print("The matrix doesn't have an inverse\n")
        elif len(matrix) == 1:
            print('The result is')
            print(-1 * matrix[0][0])
        elif len(matrix) == 2:
            matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
            matrix[0][1] = matrix[0][1] * -1
            matrix[1][0] = matrix[1][0] * -1
            matrix_by = matrix_by_constant(matrix_determinant ** -1, matrix)
            print('The result is')
            for row in matrix_by:
                print([str(round(n, 2)) for n in row])
            print('\n')
        else:
            attach_matrix = attached_matrix(matrix)
            trans_matrix = transpose_main_diagonal(attach_matrix)
            inverse = matrix_by_constant(matrix_determinant ** (-1),
                                         trans_matrix)
            for row in inverse:
                print(' '.join(str(round(n, 3)) for n in row))
    else:
        break


