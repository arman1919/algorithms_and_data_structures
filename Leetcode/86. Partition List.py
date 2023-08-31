class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def partition(self, head, x: int):
        low_head = ListNode()
        big_head = ListNode()
        curr1 = low_head
        curr2 = big_head
        curr = head
        
        while curr != None:
            if curr.val < x:
                if low_head.next == None:
                    low_head.val = curr.val
                    
                    
                    
                curr1.next = ListNode(curr.val) 
                curr1 = curr1.next
            else:
                if big_head.next == None:
                    big_head.next = ListNode(curr.val)
                    curr2 = big_head.next
                curr2.next = ListNode(curr.val) 
                curr2 = curr2.next
                
            curr = curr.next
        
        
        curr1.next = big_head.next
        return low_head.next   