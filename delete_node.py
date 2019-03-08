class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            cur.next = new_node
    def delete_node(self,data):
        new_node = Node(data)
        
        


#driver program

lst = Linkedlist()
lst.append(2)
lst.append(3)
lst.append(4)
lst.print_list()
