class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head :
                break
    def push(self,key):
        cur = self.head
        if cur is None:
            self.head = Node(key)
        else:
            new_node = Node(key)
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            return
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def remove(self,key):
        if self.head.data == key:
            cur = self.head
            while cur.next!=self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.data != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key :
                    prev.next = cur.next
                    cur = cur.next
    
            
    def josephus_circle(self,step):
        cur = self.head
        while len(self)>1 :
            count  = 1
            while count != step :
               cur = cur.next
               count +=1
            print("removed node:", str(cur.data))
            self.remove_node(cur)
            cur = cur.next



obj = stack()
obj.push(10)
obj.push(4)
obj.push(3)
obj.push(6)
obj.remove(3)
print(obj.print())
