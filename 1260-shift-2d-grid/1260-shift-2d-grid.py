class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols

        k %= total

        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                oldIdx = i * cols + j
                newIdx = (oldIdx + k) % total

                newRows = newIdx // cols
                newCols = newIdx % cols
                res[newRows][newCols] = grid[i][j]
        return res

