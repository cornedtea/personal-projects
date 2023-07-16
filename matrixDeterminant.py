""" ===================================================================

**Matrix Determinant Program**

@author: Courtney Brown <cornedtea@proton.me>

Still a work in progress, will not work yet.

"""


def findDeterminant(matrix: list, evenOdd: bool = True) -> int:
    """ Takes in a list of lists (a matrix) and finds the determinant."""
    if len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        matrix_ij = matrix.copy()
        x_ij = matrix_ij[0][0]
        if not evenOdd:
            x_ij *= -1
        for n in range(len(matrix[0])):
            del matrix_ij[n][0]
        del matrix_ij[0]
        return x_ij * findDeterminant(matrix_ij, not evenOdd)


if __name__ == "__main__":
    print(findDeterminant([[1, 2], [0, 1]]))
