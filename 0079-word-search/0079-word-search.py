class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        
        def backtracking(y : int, x : int, idx : int) :
            nonlocal found

            if board[y][x] != word[idx] :
                return
            
            if idx == len(word) - 1 :
                found = True
                return 

            visited[y][x] = 1

            for (dy, dx) in directions :
                ny = y + dy
                nx = x + dx
                if 0 <= ny < m and 0 <= nx < n :
                    if not visited[ny][nx] :
                        visited[ny][nx] = 1
                        if board[ny][nx] == word[idx + 1] :
                            backtracking(ny, nx, idx + 1)
                        visited[ny][nx] = 0

        found = False
        n, m = len(board[0]), len(board)
        for y in range(m) :
            for x in range(n) :
                visited = [[0 for _ in range(n)] for _ in range(m)]
                backtracking(y, x, idx = 0)
                    
                if found :
                    return True