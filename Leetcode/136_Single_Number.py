def singleNumber(nums: list[int]) -> int:
    unical_list = []
    for i in nums:
        if i not in unical_list:
            unical_list.append(i)
        else:
            unical_list.remove(i)
    
    return unical_list[0]
    
                
        
        

nums = [4,1,2,1,2]


print(singleNumber(nums))