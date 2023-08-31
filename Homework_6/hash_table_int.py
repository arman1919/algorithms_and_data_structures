from LinkedList import LinkedList

class MyHashTable:
    
    def __init__(self, size=100):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
        self.el_count = 0
    
    
    def hash_integer(self,n):
        A = (5 ** 0.5 - 1) / 2 
        result = n * A
        result -= int(result)  
        result *= self.size
        return int(result)
 
      
    def check_LF(self):
        lf = self.el_count / self.size
        
        if lf > 0.7:
            self.size +=  self.size//2
            self.table.extend([LinkedList() for _ in range(self.size)])
    
    
    def put(self,key,value):
        self.el_count += 1
        index = self.hash_integer(key)
        linked_list = self.table[index]
        node = linked_list.return_to_key(key)
        if node != None:
            node.value[1] = value
            return
            
            
        linked_list.add_node([key,value])
        
        self.check_LF()
        
        
        
        
    def get(self,key):
        index = self.hash_integer(key)
        linked_list = self.table[index]
        if linked_list.empty():
            raise KeyError
        
        node = linked_list.return_to_key(key)
        if node == None:
            raise KeyError
        
        return node.value[1]
    
    
    
    
    def remove(self, key):
        index = self.hash_integer(key)
        linked_list = self.table[index]
        cuurent = linked_list._head
        prev = None
        while cuurent.next is not None:
            prev = cuurent
            cuurent = cuurent.next
            if cuurent.value[0] == key:
                prev.next = cuurent.next
                self.el_count -= 1
                return
        raise KeyError(key)
        
    
        
        
        
            

ht = MyHashTable(10)

ht.put(1,15)
ht.put(2,16)
ht.put(3,17)
ht.put(4,18)
ht.put(5,15)
ht.put(6,16)
ht.put(7,17)
ht.put(8,18)

for i in ht.table:
    print(i)
    
print()

ht.put(9,18)

ht.remove(9)

for i in ht.table:
    print(i)


print(ht.size)
    


            
        
        
        


