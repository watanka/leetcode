import sys
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        # board is Boustrophedon style
        N = len(board)

        def square2coord(square_num) : 
            nrow = N - square_num // N - (1 if square_num % N else 0)
            if (nrow - N) % 2: 
                ncol = square_num % N - (1 if square_num % N else -N+1)
            else :
                ncol = N - (square_num % N if square_num % N else N)

            return (nrow, ncol)

        def coord2square(coord) :
            nrow, ncol = coord
            
            squarenum = 0
            squarenum += (nrow - N + 1) * N

            if (nrow - N) % 2 : # from left to right
                squarenum += ncol + 1
            else :
                squarenum += N - ncol 
            return squarenum



    
        minNum = sys.maxsize
        visited = [0 for _ in range(N*N+1)]   

        queue = collections.deque([[1, 0]])

        
        while queue :
            cur_square, cnt = queue.popleft()
            if not visited[cur_square] :
                visited[cur_square] = 1
                for step in range(1, 7) :
                    new_square = cur_square + step
                    if 1 <= new_square <= N * N :
                        new_y, new_x =  square2coord(new_square)
                        if board[new_y][new_x] != -1 :
                            new_square = board[new_y][new_x]
                        if new_square == N*N :
                            return cnt + 1
                        queue.append([new_square, cnt + 1])

        return -1
