# binary_search (recursive) in Python


def binary_search(arr:list,target:int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:
            right = mid -1 
            mid == (left+right) // 2
        
        else:
            left = mid +1 
            mid == (left+right) // 2
            
    
    return "Target not found"

 

def binary_search_recursive(arr:list,target:int,left,right):
    
    mid = (left+right) // 2
    
   
    
    if left > right:
        
        return "Target not found"
    
    
    elif arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search_recursive(arr,target,0,mid-1)
           
    else:
        return binary_search_recursive(arr,target,mid+1,len(arr)-1)

        
            
    


ls = [1,2,3,4,5,6,7,8,9]

print(binary_search(ls,1))
print(binary_search(ls,5))
print(binary_search(ls,9))
print(binary_search(ls,12))
print()
print(binary_search_recursive(ls,1,0,len(ls)-1))
print(binary_search_recursive(ls,6,0,len(ls)-1))
print(binary_search_recursive(ls,9,0,len(ls)-1))
print(binary_search_recursive(ls,12,0,len(ls)-1))





        



    