def AMB(x,y):
    if x > y:
        x,y = y,x
    
    for i in range(x / 2,0,-1):
        if x % i  == 0 and y % i == 0:
            return i
        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def insertGreatestCommonDivisors(head):
    current = head
    
    while current != None and current.next != None:
        num = AMB(current.val,current.next.val)
        new_node = ListNode(num,current.next)
        
        current.next = new_node
        current = new_node.next
        
    
    return head
        
        
