class  Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def delete(self,key):
        cur = self.head
        if (cur and cur.data==key):
            self.head = cur.next
            cur = None
        while (cur and cur.data!=key):
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
    def delete_nth_node(self,n):
        cur = self.head
        len = 0
        while cur:
            cur = cur.next
            len += 1
        if n>len :
            print('given number is out of index of linkedlist')
        cur = self.head
        for _ in range(0,len-n-1):
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None   

lst = linkedlist()
lst.push(2)
lst.push(3)
lst.push(4)
lst.push(5)
lst.push(6)
lst.push(7)
#lst.delete(4)
lst.delete_nth_node(3)
lst.print()