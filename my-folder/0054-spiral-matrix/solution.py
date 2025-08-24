class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        while matrix:     
            output += matrix.pop(0)

            if matrix and matrix[0]:
                for col in matrix:
                    output.append(col.pop())

            if matrix:
                output += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for col in matrix[::-1]: #reversed
                    output.append(col.pop(0))
        return output



        
