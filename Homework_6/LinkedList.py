class Node:
    def __init__(self,value = None,next = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self._head = Node()
        
    def empty(self):
        if self._head.next == None:
            return True
        return False
    
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
        
        
    def clear(self):
        self._head.next = None
        
    
    def check_el(self,x):
        cuurent = self._head
        
        while cuurent != None:
            if cuurent.value[0] == x:
                return True
            cuurent = cuurent.next
            
        return False
    
    def return_to_key(self,key):
        
        cuurent = self._head.next
        
        while cuurent != None:
            if cuurent.value[0] == key:
                return cuurent
            cuurent = cuurent.next
        return None


