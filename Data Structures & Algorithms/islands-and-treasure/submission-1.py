from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while q:
            r,c=q.popleft()
            for i,j in directions:
                dr=i+r
                dc=j+c
                if (0<=dr<m and 0<=dc<n and grid[dr][dc]==2147483647):
                    grid[dr][dc]=grid[r][c]+1
                    q.append((dr,dc))