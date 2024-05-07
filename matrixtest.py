import unittest
from matrix import *

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[2, 0], [1, 2]])
        self.matrix3 = Matrix([[3, 6], [9, 12]])

    def test_addition(self):
        result = self.matrix1 + self.matrix2
        expected = Matrix([[3, 2], [4, 6]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_subtraction(self):
        result = self.matrix1 - self.matrix2
        expected = Matrix([[-1, 2], [2, 2]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_multiplication(self):
        result = self.matrix1 * self.matrix2
        expected = Matrix([[4, 4], [10, 8]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_transpose(self):
        result = self.matrix1.transpose()
        expected = Matrix([[1, 3], [2, 4]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_determinant(self):
        result = self.matrix1.determinant()
        self.assertEqual(result, -2)

    def test_inverse(self):
        result = self.matrix1.inverse()
        expected = Matrix([[-2, 1], [1.5, -0.5]])
        for i in range(len(expected.matrix)):
            for j in range(len(expected.matrix[i])):
                self.assertAlmostEqual(result.matrix[i][j], expected.matrix[i][j])

    def test_scalar_multiply(self):
        result = self.matrix1.scalar_multiply(3)
        expected = Matrix([[3, 6], [9, 12]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_identity(self):
        result = Matrix.identity(2)
        expected = Matrix([[1, 0], [0, 1]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_power(self):
        result = self.matrix1.power(2)
        expected = self.matrix1 * self.matrix1
        self.assertEqual(result.matrix, expected.matrix)

    def test_division_by_scalar(self):
        result = self.matrix3 / 3
        expected = self.matrix1
        self.assertEqual(result.matrix, expected.matrix)

    def test_equality(self):
        self.assertTrue(self.matrix1 == Matrix([[1, 2], [3, 4]]))
        self.assertFalse(self.matrix1 == self.matrix2)

    def test_inequality(self):
        self.assertTrue(self.matrix1 != self.matrix2)
        self.assertFalse(self.matrix1 != Matrix([[1, 2], [3, 4]]))

if __name__ == '__main__':
    unittest.main()
