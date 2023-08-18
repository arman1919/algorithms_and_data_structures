import typing

class Stack():

    def __init__(self) -> None:
        self.stack = []
        self.index = -1
    
    def push(self,element:typing.Any):
        self.stack.append(element)
        self.index +=1
        
    def size(self):
        
        return self.index+1
    
    
    def pop(self):
        temp = self.stack[-1]
        self.stack.pop()
        self.index -= 1
        return temp
    
    def top(self):
        return self.stack[self.index]
    
    def __str__(self) -> str:
        res = ''
        for i in self.stack:
            res += str(i) + ", "
        return res 
    
    
        


s= Stack()
s.push(15)
s.push("aa")
print("size = ",s.size())

s.push(25)

print("top = ",s.top())

s.pop()

print("top = ",s.top())


       