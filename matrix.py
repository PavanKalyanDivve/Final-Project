class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns of the first matrix must be equal to the number of rows of the second matrix")
        result = []
        for i in range(self.rows):
            result_row = []
            for j in range(other.cols):
                sum_product = 0
                for k in range(self.cols):
                    sum_product += self.matrix[i][k] * other.matrix[k][j]
                result_row.append(sum_product)
            result.append(result_row)
        return Matrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to find the determinant")
        return self._determinant_recursive(self.matrix)

    def _determinant_recursive(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1) ** c) * matrix[0][c] * self._determinant_recursive(self._get_minor(matrix, 0, c))
        return determinant

    def _get_minor(self, matrix, row, col):
        return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to find the inverse")
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        matrix_minor = [[self._determinant_recursive(self._get_minor(self.matrix, i, j)) for j in range(self.cols)] for i in range(self.rows)]
        cofactors = [[matrix_minor[i][j] * ((-1) ** (i + j)) for j in range(self.cols)] for i in range(self.rows)]
        adjugate = Matrix(cofactors).transpose()
        inverse_matrix = [[adjugate.matrix[i][j] / det for j in range(adjugate.cols)] for i in range(adjugate.rows)]
        return Matrix(inverse_matrix)

    def scalar_multiply(self, scalar):
        result = [[self.matrix[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    @staticmethod
    def identity(size):
        result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        return Matrix(result)

    def power(self, n):
        if n == 0:
            return Matrix.identity(self.rows)
        elif n == 1:
            return self
        elif n > 1:
            result = self
            for _ in range(n - 1):
                result = result * self
            return result

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.matrix[i][j] / other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        else:
            raise ValueError("Matrix division is not supported")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __ne__(self, other):
        return not self.__eq__(other)