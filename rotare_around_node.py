class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def rotate_around_node(self,k):
        p = q = self.head
        prev = None
        count = 0
        while p and count<k :
            prev = p
            p = p.next
            q = q.next
            count+=1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None


obj = linkedlist()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)            
obj.append(17)
obj.append(8)
obj.append(12)
obj.append(0)
	
obj.rotate_around_node(4)
obj.print_list()
