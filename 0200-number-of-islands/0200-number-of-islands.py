from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        # bfs
        num_islands = 0

        def bfs(j, i) :
            queue = deque([(j, i)])
            while queue :
                y, x = queue.popleft()
                for dy, dx in directions :
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < m and 0 <= nx < n :
                        if grid[ny][nx] == "1" :
                            grid[ny][nx] = '-1'
                            queue.append((ny, nx))
        
        for j in range(m) :
            for i in range(n) :
                if grid[j][i] == "1" :
                    bfs(j, i)
                    num_islands += 1

        return num_islands


            