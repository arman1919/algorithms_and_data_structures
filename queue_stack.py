class MyStack:

    def __init__(self):
        self.ls = []
        self.i = 0

    def push(self, x: int) -> None:
        self.ls.append(x)
        
        

    def pop(self) -> int:
        el = self.ls[-1]
        
        self.ls.pop(-1)
        return el
            
        

    def top(self) -> int:
        return self.ls[-1]
    
        

    def empty(self) -> bool:
        if len(self.ls) == 0:
            return True
        
        return False
    
    def size(self):
        return len(self.ls)

    def prin(self):
        for i in self.ls:
            print(i,end=", ")
           
class MyQueue:

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()
        

    def push(self, x: int) -> None:
        
        
        while not self.s1.empty():

            self.s2.push(self.s1.pop())             #  s1 
                                  
        self.s2.push(x)          
        
        while not self.s2.empty():
            
            self.s1.push(self.s2.pop())
        
       

    def pop(self) -> int:
        
        return self.s1.pop()
    
    

    def peek(self) -> int:
        
        return self.s1.top()

    def empty(self) -> bool:
        if self.s1.empty() and self.s2.empty():
            return True
        
        return False




q = MyQueue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.peek())
print(q.pop())
