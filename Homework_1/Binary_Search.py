

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





ls = [1,2,3,4,5,6,7,8,9]

print(binary_search(ls,5))
print(binary_search(ls,12))




        



    