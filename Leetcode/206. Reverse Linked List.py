def reverseList(head):
        if head == []: 
            return []
        
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev