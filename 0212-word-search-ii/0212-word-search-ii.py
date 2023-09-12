class TrieNode :
    def __init__(self) :
        self.children = {}
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, root) :
            letter = board[x][y]
            cur = root[letter]

            word = cur.pop('#', False)
            if word :
                res.append(word)
            board[x][y] = '*'

            for dirx, diry in [(0,1),(0,-1), (1,0), (-1, 0)] :
                curx, cury = x + dirx, y + diry

                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur :
                    dfs(curx, cury, cur)

            board[x][y] = letter

            if not cur :
                root.pop(letter)

        trie = {}
        for word in words :
            cur = trie
            for c in word :
                cur = cur.setdefault(c, {})
            cur['#'] = word

        m, n = len(board), len(board[0])
        res = []

        for i in range(m) :
            for j in range(n) :
                if board[i][j] in trie :
                    dfs(i, j, trie)

        return res