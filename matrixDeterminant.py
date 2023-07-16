""" ===================================================================

**Matrix Determinant Program**

@author: Courtney Brown <cornedtea@proton.me>

Still a work in progress, will not work yet.

"""


def det(matrix: list, evenOdd: bool = True, i: int = -1, j: int = -1, row_i: list = [], col_j: list = []):
    """
    Takes in a list of lists (a matrix) and finds the determinant.
    """
    if len(matrix[0]) != len(matrix):
        return "Error: Cannot calculate determinant of non-square matrix."
    elif len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        # if i < len(matrix):
        #     i += 1
        #     j += 1
        if len(row_i) != 0 and len(col_j) != 0:
            matrix.insert(i, row_i)
            for n in range(len(matrix)):
                matrix[n].insert(j, col_j[n])
        x_ij = matrix[0][0]
        if not evenOdd:
            x_ij *= -1
        for n in range(len(matrix)):
            col_j.append(matrix[n].pop(j))
        row_i = matrix.pop(i)
        return x_ij * det(matrix, not evenOdd, i, j, row_i, col_j)


if __name__ == "__main__":
    matrix_A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(det(matrix_A))
