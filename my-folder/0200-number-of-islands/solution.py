class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        directions = [[1,0],[-1,0], [0,1], [0,-1]]


        row_len, col_len = len(grid), len(grid[0])
        visited = set()
        def sink_neighbors(r,c):
            q = [(r,c)]
            visited.add((r,c))
            while q:
                row, col = q.pop(0)
                for nr,nc in directions:
                    ur, uc = row + nr, col + nc
                    if 0<= ur < row_len and 0 <= uc < col_len and grid[ur][uc] == '1' and (ur, uc) not in visited:
                      q.append((ur, uc))
                      visited.add((ur, uc)) 


        islands = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    sink_neighbors(r,c)

        return islands

