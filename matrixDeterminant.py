""" ===================================================================

**Matrix Determinant Program**

@author: Courtney Brown <cornedtea@proton.me>

Progress:
* diagonalDet() can find the determinant of a diagonal matrix.

Still working on:
* Cofactor expansion in det()

"""


def diagonalDet(matrix: list):
    """
    Takes in a diagonal matrix (list of lists) and finds the determinant.
    """
    if len(matrix) == 0:
        return "Error: Cannot calculate determinant of empty matrix."
    if len(matrix[0]) != len(matrix):
        return "Error: Cannot calculate determinant of non-square matrix."
    if len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        matrix_ij = matrix.copy()
        x_ij = matrix_ij[0][0]
        for n in range(len(matrix_ij)):
            del matrix_ij[n][0]
        del matrix_ij[0]
        return x_ij * diagonalDet(matrix_ij)


def det(matrix: list, evenOdd: bool = True, i: int = 0, j: int = 0, row_i: list = [], col_j: list = []):
    """
    Takes in a list of lists (a matrix) and finds the determinant.
    """
    if len(matrix) == 0:
        return "Error: Cannot calculate determinant of empty matrix."
    if len(matrix[0]) != len(matrix):
        return "Error: Cannot calculate determinant of non-square matrix."
    if len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        matrix_ij = matrix.copy()
        # if i < len(matrix_ij):
        #     i += 1
        #     j += 1
        # if len(row_i) != 0 and len(col_j) != 0:
        #     matrix_ij.insert(i, row_i)
        #     for n in range(len(matrix_ij)):
        #         matrix_ij[n].insert(j, col_j[n])
        x_ij = matrix_ij[0][0]
        if not evenOdd:
            x_ij *= -1
        for n in range(len(matrix_ij)):
            col_j.append(matrix_ij[n].pop(j))
        row_i = matrix_ij.pop(i)
        # return x_ij * det(matrix_ij, not evenOdd, i, j, row_i, col_j)


if __name__ == "__main__":
    matrix_A = [[1, 0, 0], [0, 6, 0], [0, 0, 2]]
    matrix_D = [[1, 2], [1, 2]]

    assert diagonalDet(matrix_A) == 12
    # assert det(matrix_A) == 12
    # assert det(matrix_D) == 0
