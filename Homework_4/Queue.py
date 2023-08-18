import typing

class _Queue():
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def Enqueue(self,element : typing.Any):
        self._queue.append(element)
        self._index += 1
        
        
    def Dequeue(self):
        temp = self._queue[0]
        self._queue.pop(0)
        self._index -= 1

        return temp
    
    def size(self):
        size = 0
        for i in self._queue:
            size += 1
        
        return size

    def top(self):
        return self._queue[self._index]
    
    def empty(self):
        
        if self.size() == 0:
            return True
        
        return False
    
    
            
    def __str__(self) -> str:
        res = ""
        for i in self._queue:
            res += i + ", "
        return res
    
    
    
    

q = _Queue()

if q.empty():
    print("queue is empty")
    
q.Enqueue("Human 1")
q.Enqueue("Human 2")
q.Enqueue("Human 3")

print("size =", q.size())

print(q)

print("out of the _queue",q.Dequeue())

print(q)

q.Enqueue("Human 4")

print(q)



