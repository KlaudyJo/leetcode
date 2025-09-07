class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # rows
        n = len(matrix[0]) # columns

        t = m * n
        l , r = 0, t-1

        while l <= r:
            m = (l+r) // 2

            i = m //n # row index
            j = m % n # column index

            min_num = matrix[i][j]
            if min_num == target:
                return True

            elif target < min_num:
                r = m - 1
            else:
                l = m + 1

        return False

            

