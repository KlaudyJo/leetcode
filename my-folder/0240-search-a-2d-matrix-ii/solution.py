class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])

        r, c = 0, cols - 1

        while r < rows and c >= 0:
            num = matrix[r][c]

            if num == target:
                return True

            elif num > target:
                c -= 1
            else:
                r += 1
        return False
        
