class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## 2nd approach. dfs on only border
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        flip = []

        ## mark the borderline Os and stack on stack.
        for j in range(m) :
            for i in range(n) : 
                if board[j][i] == 'O' :
                    if j * i == 0 or j == m - 1 or i == n - 1 :
                        flip.append((j, i))
                        board[j][i] = '*'

        while flip :
            y, x = flip.pop()
            for dy, dx in directions :
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n :
                    if board[ny][nx] == 'O' :
                        board[ny][nx] = '*'
                        flip.append((ny, nx))


        for j in range(m) :
            for i in range(n) :
                if board[j][i] == '*' : 
                    board[j][i] = 'O'
                else :
                    board[j][i] = 'X'



        # 1st approach. dfs
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # m, n = len(board), len(board[0])
        # # if contact to the border, change it to 'X'
        # flip = []

        # def dfs(stack, color) :
        #     nonlocal flip 
        #     on_border = False
        #     while stack :
        #         y, x = stack.pop()
        #         board[y][x] = color
        #         for dy, dx in directions :
        #             ny, nx = y + dy, x + dx

        #             if 0 <= ny < m and 0 <= nx < n :
        #                 if board[ny][nx] == 'O' :
        #                     stack.append((ny, nx))

        #             else :
        #                 on_border = True
        #     if not on_border :
        #         flip.append(color)


        # color = 0
        # for j in range(m) :
        #     for i in range(n) :
        #         if board[j][i] == 'O' : 
        #             dfs([(j, i)], color)
        #             color += 1

        # for j in range(m) :
        #     for i in range(n) :
        #         if board[j][i] in flip :
        #             board[j][i] = 'X'
        #         elif board[j][i] != 'X' : #or board[j][i] != 'O' :
        #             board[j][i] = 'O'


