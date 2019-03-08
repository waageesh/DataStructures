class Node:
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
    def swap(self,x,y):
        curX = curY = self.head
        prevX = prevY = None  

        if x == y:
            return

        while curX and curX.data != x :
            prevX = curX
            curX = curX.next
        while curY and curY.data != y :
            prevY = curY
            curY = curY.next

        if not curX or not curY:
            return

        if prevX:
            prevX.next = curY            
        else:
            self.head = curY

        if prevY:
            prevY.next = curX
        else:
            self.head = curX
        #print(curX.next , curY.next)
        curX.next , curY.next = curY.next , curX.next
    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


obj = linkedlist()
obj.push(1)
obj.push(2)
obj.push(5)
obj.push(6)
obj.push(9)
obj.push(7)
obj.swap(9,5)
print("original sequence: 7 -> 9 -> 6 -> 5 -> 2 -> 1")
print("expected output : 7 -> 5 -> 6 -> 9 -> 2 -> 1")
obj.print()
