class node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        # left -> LRU and right= MRU
        self.left,self.right=node(0,0), node(0,0)
        self.left.next,self.right.prev=self.right,self.left

    #remove from left
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    #insert node at right
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            #remove the value from the list and delete LRU from hashmap
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]






        
