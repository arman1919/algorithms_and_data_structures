class Node:
    def __init__(self, value=None, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class doubly_linkedList:
    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def push_back(self, value):
        new_node = Node(value, prev=self._tail.prev, next=self._tail)
        self._tail.prev.next = new_node
        self._tail.prev = new_node

    def __str__(self) -> str:
        if self._head.next == self._tail:
            return "empty"
        current = self._head.next
        s = ''

        while current != self._tail:
            s += str(current.value) + ", "
            current = current.next

        return s

    def pop_back(self):
        if self._tail.prev == self._head:
            print("LinkedList empty")
            return

        self._tail.prev = self._tail.prev.prev
        self._tail.prev.next = self._tail

    def get_size(self):
        current = self._head.next
        s = 0
        while current != self._tail:
            current = current.next
            s += 1
        return s


    def push_pos(self, pos, value):
        if self.get_size() < pos or pos < 1:
            raise IndexError

        i = 1
        current = self._head
        while i < pos:
            current = current.next
            i += 1

        new_node = Node(value, prev=current, next=current.next)
        current.next.prev = new_node
        current.next = new_node

    def erase(self, pos):
        if self.get_size() < pos or pos < 1:
            raise IndexError

        i = 1
        current = self._head
        while i < pos:
            current = current.next
            i += 1

        current.next = current.next.next
        current.next.prev = current

    def print_reverse(self):
        current = self._tail.prev
        while current != self._head:
            print(current.value, end=", ")
            current = current.prev
        print()


    def clear(self):
        self._head.next = None
        self._tail.prev = None
    
    def empty(self):
        return self._head.next == None

    def push_front(self,value):
        new_node = Node(value,self._head,self._head.next)
        if self._head.next != None:
            temp = self._head.next
            self._head.next.prev = new_node
        self._head.next = new_node
         
    def front(self):
        return self._head.next.value 

    def back(self):
        return self._tail.prev.value

    def resize(self,new_size):
        if new_size > self.get_size()  or new_size < 0:
            raise ValueError
        current = self._head
        for _ in  range(0,new_size):
              current = current.next
        
        current.next = self._tail
        self._tail.prev = current
        



ll = doubly_linkedList()

ll.push_back(5)
ll.push_back(1)
ll.push_back(6)
ll.push_back(3)
ll.push_back(7)
ll.push_back(4)
ll.push_back(2)


print(ll)

ll.erase(2)

print(ll)

print(ll.front())

print(ll.back())




