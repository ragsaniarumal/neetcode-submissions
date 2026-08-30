class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head

        for i in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            new_node.next = None
            self.size += 1
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = new_node

        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        l = []
        
        curr = self.head
        while curr:
            l.append(curr.val)
            curr = curr.next
        
        return l
