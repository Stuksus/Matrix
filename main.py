file_name = input("filename: ")
matrix_test = []
file = open(file_name)
for line in file:
    final_line = map(int, line.strip("\n").split(" "))
    matrix_test.append(list(final_line))
file.close()
print(matrix_test)


def find_max_count_zero(matrix):  # return [...]: [0]-count zero, [1]-index columns or rows, [2]='1' rows or '0' columns
    maximum_zero_rows = [-(2 ** 32), 0, 1]
    maximum_zero_colms = [-(2 ** 32), 0, 0]

    for i in range(len(matrix)):
        count_zero_rows = 0
        count_zero_colms = 0
        for j in matrix[i]:
            if j == 0:
                count_zero_rows += 1
            if count_zero_rows > maximum_zero_rows[0]:
                maximum_zero_rows[0] = count_zero_rows
                maximum_zero_rows[1] = i

        for h in range(len(matrix)):

            if matrix[h][i] == 0:
                count_zero_colms += 1
            if count_zero_colms > maximum_zero_colms[0]:
                maximum_zero_colms[0] = count_zero_colms
                maximum_zero_colms[1] = i

    if maximum_zero_rows[0] > maximum_zero_colms[0]:
        return maximum_zero_rows
    elif maximum_zero_colms[0] > maximum_zero_rows[0]:
        return maximum_zero_colms
    elif maximum_zero_colms[0] == maximum_zero_rows[0] and maximum_zero_colms[0] != 0:
        return maximum_zero_rows
    else:
        return [0, 0, 0]


def elemental_procedure(matrix, zero_info):
    if zero_info == [0, 0, 0]:
        for i in range(1, len(matrix)):
            factor = -(matrix[i][0]) / matrix[0][0]
            for j in range(len(matrix[i])):
                matrix[i][j] += matrix[0][j] * factor
        return matrix, 0
    elif zero_info[0] == (len(matrix)):
        return [-10, -10, -10], 0
    elif zero_info != [0, 0, 0] and zero_info[2] == 1:
        non_zero_index = -1
        count = len(matrix[zero_info[1]])
        while non_zero_index == -1 and count > 0:
            if matrix[zero_info[1]][count - 1] != 0:
                non_zero_index = count - 1
            count -= 1

        for i in range(len(matrix[zero_info[1]])):
            if [i] != [non_zero_index]:
                factor = -(matrix[zero_info[1]][i]) / matrix[zero_info[1]][non_zero_index]
                for j in range(len(matrix)):
                    matrix[j][i] += factor * matrix[j][non_zero_index]
        return matrix, non_zero_index
    elif zero_info != [0, 0, 0] and zero_info[2] == 0:
        non_zero_index = -1
        count = len(matrix)
        while non_zero_index == -1 and count > 0:
            if matrix[count - 1][zero_info[1]] != 0:
                non_zero_index = count - 1
            count -= 1
        for i in range(len(matrix)):
            if i != non_zero_index:
                factor = -(matrix[i][zero_info[1]]) / matrix[non_zero_index][zero_info[1]]
                for j in range(len(matrix[i])):
                    matrix[i][j] += (factor * matrix[non_zero_index][j])
        return matrix, non_zero_index


def minor(matrix, zero_info, minor_index):
    mini_matrix = []
    if zero_info[2] == 0:
        for i in range(len(matrix)):
            micro = []
            if i != minor_index:
                for j in range(len(matrix[i])):
                    if j != zero_info[1]:
                        micro.append(matrix[i][j])
                mini_matrix.append(micro)
        return mini_matrix
    elif zero_info[2] == 1:
        for i in range(len(matrix)):
            micro = []
            if i != zero_info[1]:
                for j in range(len(matrix[i])):
                    if j != minor_index:
                        micro.append(matrix[i][j])
                mini_matrix.append(micro)

        return mini_matrix


multi = 1
answer = 10
for i in range(len(matrix_test) - 1):

    mark = 1
    info_zero = find_max_count_zero(matrix_test)
    new_matrix, index = elemental_procedure(matrix_test, info_zero)
    if new_matrix == [-10, -10, - 10]:
        answer = 0
        break
    elif info_zero[2] == 1:
        if (info_zero[1] + index) % 2 != 0:
            mark = -1
        multi *= new_matrix[info_zero[1]][index] * mark

    elif info_zero[2] == 0:
        if (info_zero[1] + index) % 2 != 0:
            mark = -1
        multi *= new_matrix[index][info_zero[1]] * mark

    matrix_test = minor(new_matrix, info_zero, index)
if answer == 0:
    print("answer: ", answer)
else:
    print("answer: ", round(matrix_test[0][0] * multi))
