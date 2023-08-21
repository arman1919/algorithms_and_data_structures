class SelfOrganizingNode:
    def __init__(self, value=None, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class SelfOrganizingLinkedList:
    def __init__(self) -> None:
        self._head = SelfOrganizingNode()
        self._tail = SelfOrganizingNode()
        self._head.next = self._tail
        self._tail.prev = self._head

    def add_node(self, value):
        new_node = SelfOrganizingNode(value, prev=self._tail.prev, next=self._tail)
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

    def move_to_front(self, value):
        current = self._head.next
        while current != self._tail:
            if current.value == value:
                
                current.prev.next = current.next
                current.next.prev = current.prev
                current.prev = self._head
                current.next = self._head.next
                self._head.next.prev = current
                self._head.next = current
                return
            current = current.next

    def add_node_pos(self, pos, value):
        if self.get_size() < pos or pos < 1:
            raise IndexError

        i = 1
        current = self._head
        while i < pos:
            current = current.next
            i += 1

        new_node = SelfOrganizingNode(value, prev=current, next=current.next)
        current.next.prev = new_node
        current.next = new_node

    def pop_node_pos(self, pos):
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



ll = SelfOrganizingLinkedList()

ll.add_node(5)
ll.add_node(1)
ll.add_node(6)
ll.add_node(3)
ll.add_node(7)
ll.add_node(4)
ll.add_node(2)

print(ll)

ll.move_to_front(7)

print(ll)

