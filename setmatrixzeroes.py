class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        for c in column:
            for j in range(len(matrix)):
                matrix[j][c] = 0
        return matrix
