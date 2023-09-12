class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])

        trie = {}
        for word in words :
            cur = trie
            for letter in word :
                cur = cur.setdefault(letter, {})
            cur['#'] = word

        def dfs(y, x, node) :
            letter = board[y][x]
            cur = node[letter]

            word = cur.pop('#', False)
            if word :
                result.append(word)
    

            board[y][x] = '*'

            for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and board[ny][nx] in cur :
                    dfs(ny, nx, cur)
                
            board[y][x] = letter

            if not cur :
                node.pop(letter)


        result = []
        for y in range(m) :
            for x in range(n) :
                if board[y][x] in trie :
                    dfs(y, x, trie)

        return result