class Node :
    def __init__(self, key = -1, val = -1, prev = None, next = None) :
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, newNode) :
        tmp = self.head.next
        newNode.next = tmp
        newNode.prev = self.head
        self.head.next = newNode
        tmp.prev = newNode

    def deleteNode(self, delNode) :
        prevv = delNode.prev
        nextt = delNode.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.dic :
            resNode = self.dic[key]
            ans = resNode.val
            del self.dic[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.dic[key] = self.head.next
            return ans
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic :
            curr = self.dic[key]
            del self.dic[key]
            self.deleteNode(curr)

        if len(self.dic) == self.capacity :
            del self.dic[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        
        self.addNode(Node(key, value))
        self.dic[key] = self.head.next
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)