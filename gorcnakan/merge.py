
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge_sorted_lists(self, list1, list2):

        if list1 == []:
            return list2
        if list2 == []:
            return list1
        
        merged_list = ListNode()
        current = merged_list
        current_list1 = list1
        current_list2 = list2

        while current_list1 is not None and current_list2 is not None:
            if current_list1.value < current_list2.value:
                current.next = current_list1
                current = merged_list.next
                current_list1 = current_list1.next
            else:
                merged_list.next = current_list2
                current = merged_list.next
                current_list2 = current_list2.next
        
        while current_list1.next is not None:
            merged_list.next = current_list2
            current = merged_list.next
            current_list2 = current_list2.next

        while current_list2.next is not None:
            merged_list.next = current_list2
            current = merged_list.next
            current_list2 = current_list2.next

       
        return merged_list