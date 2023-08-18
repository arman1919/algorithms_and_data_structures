
class D_arr:
    def __init__(self,size = 0) -> None:
        self.size = 0
        
        # for large numbers
        self.copasity = round(size*self.get_relation(size))
        self.Darr = self.copasity*[None]
        
        
    
    @staticmethod
    def get_relation(num):
        
        if 0 < num < 1000:
            return 2
        else:    # for large numbers
            return 1.1 
        

    def __str__(self) -> str:
        return str(self.Darr)
    
    def get_size(self):
        if self.Darr == []:
            return 0
        i = 0
        while self.Darr[i] != None:
            i += 1
        
        return i
    
    def get_cop(self):
        return self.copasity     
        
        
    def push_back(self,el):
        if self.Darr == []:
            self.size = 1
            self.copasity = 2
            self.Darr = [None]*2
            
            self.Darr[0] = el 
            
        else:
            i = 0
            while self.Darr[i] != None:
                i += 1
                
                
            self.Darr[i] = el
            self.size +=1
            
            self.update_arr()
    
    
    def update_arr(self):
        if self.size == self.copasity:
            self.copasity = round(self.size*self.get_relation(self.size))
            new_arr = [None] * self.copasity
            for i in range(self.size):
                new_arr[i] = self.Darr[i]
            
            self.Darr = new_arr
          
          
    def insert(self,pos,value):
        i  = self.size-1
        while i+1 !=  pos:
            self.Darr[i],self.Darr[i+1] = self.Darr[i+1],self.Darr[i]
            i -= 1
        self.Darr[i+1] = value
        self.size += 1
        self.update_arr()
        

    def insert_many(self,pos,value,count):
        for _ in range(count):
            self.insert(pos,value)
        
        

    def pop_back(self):
        if self.Darr == []:
            print("Arr empty")
            return
        
        for i in range(self.size):
            if self.Darr[i+1] == None:
                self.Darr[i] = None
                break
            
        self.size -= 1
    
    def remove(self,pos):
        if self.size-1<pos<0:
            raise IndexError
        
        i = pos
        while self.Darr[i+1] != None:
            self.Darr[i],self.Darr[i+1] = self.Darr[i+1],self.Darr[i]         
            i+=1
        self.Darr[i] = None
        
    
    def empty(self):
        return self.Darr == []

    def clerar(self):
        self.Darr = []
    
    
d = D_arr(0)

d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)
d.push_back(15)

print(d)
print(d.get_cop(),d.get_size(),d.size)

d.insert(5,5)
print(d)
d.insert_many(2,2,2)
print(d)
d.pop_back()
print(d)
d.remove(11)
print(d)





