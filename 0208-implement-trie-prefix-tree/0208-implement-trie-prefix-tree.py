class Trie:

    def __init__(self):
        self.ls = []
        

    def insert(self, word: str) -> None:
        self.ls.append(word)
        

    def search(self, word: str) -> bool:
        for search_ in self.ls :
            if search_ == word :
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for search_ in self.ls :
            if search_.startswith(prefix) :
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)