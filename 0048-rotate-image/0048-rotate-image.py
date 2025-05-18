class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            for j in range(int(len(matrix[i]) / 2)):
                swapJ = len(matrix[i]) - j - 1   

                temp = matrix[i][j]
                matrix[i][j] = matrix[i][swapJ]
                matrix[i][swapJ] = temp
   