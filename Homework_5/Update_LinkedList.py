class Node:
    def __init__(self,value = None,next = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self._head = Node()
        
    
    def add_node(self,value):
        cuurent = self._head
        while cuurent.next != None:
            cuurent = cuurent.next
        
        new_node = Node(value)
        cuurent.next = new_node
        
    
    
    
    
    def __str__(self) -> str:
        if self._head.next ==  None:
            return "empty"
        cuurent = self._head
        s = ''
        
        while cuurent.next != None:
            if cuurent is self._head:
            
                cuurent = cuurent.next
            else:
                s += str(cuurent.value)+", "
                cuurent = cuurent.next
                
        
        s += str(cuurent.value)+", "
        
        return s        
        
    def pop_back(self):
        if self._head.next == None:
            print("LinkedList empty")
            return
        elif self._head.next.next == None:
            self._head.next = None
            return
            
        cuurent = self._head
        while cuurent.next.next != None:
            cuurent = cuurent.next
            
        cuurent.next = None
    
    def get_size(self):
        if self._head.next == None:
            return 0
        
        cuurent = self._head
        s = 0
        while cuurent.next != None:
            cuurent = cuurent.next
            s+=1
        return s    

    def add_node_pos(self,pos,value):
        if  self.get_size()<pos or pos<1:
            raise IndexError
        
        i = 1
        cuurent = self._head
        while pos != i:
            cuurent = cuurent.next    
            i +=1
        
        
        
        new_node = Node(value,cuurent.next)
        cuurent.next = new_node
        
    def pop_node_pos(self,pos):
        if  self.get_size()<pos or pos<1:
            raise IndexError
            
        
        i = 1
        cuurent = self._head
        while pos != i:
            cuurent = cuurent.next    
            i +=1
        
        cuurent.next = cuurent.next.next
        
    def reverse(self):
        prev = None
        current = self._head.next

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        
        self._head.next = prev
            
    
    def split(self):
        if self._head.next is None:
            
            return None, None

        slow_ptr = self._head
        fast_ptr = self._head

        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        
        first_half = self
        second_half = LinkedList()
        second_half._head.next = slow_ptr.next
        slow_ptr.next = None

        return first_half, second_half
    
    
    
    def merge_sort(self):
        if self.get_size() <= 1:
            
            return

        
        first_half, second_half = self.split()

        
        if first_half is not None:
            first_half.merge_sort()
        if second_half is not None:
            second_half.merge_sort()

        
        self.merge_sorted_lists(first_half, second_half)

    def merge_sorted_lists(self, list1, list2):
        
        merged_list = LinkedList()

        current_list1 = list1._head.next
        current_list2 = list2._head.next

        while current_list1 is not None and current_list2 is not None:
            if current_list1.value < current_list2.value:
                merged_list.add_node(current_list1.value)
                current_list1 = current_list1.next
            else:
                merged_list.add_node(current_list2.value)
                current_list2 = current_list2.next

        
        while current_list1 is not None:
            merged_list.add_node(current_list1.value)
            current_list1 = current_list1.next

        while current_list2 is not None:
            merged_list.add_node(current_list2.value)
            current_list2 = current_list2.next

       
        self._head = merged_list._head

        
   
        
    def clear(self):
        self._head.next = None
        
        
ll = LinkedList()

ll.add_node(5)
ll.add_node(1)
ll.add_node(6)
ll.add_node(3)
ll.add_node(7)
ll.add_node(4)
ll.add_node(2)

ll.merge_sort()

print(ll)
