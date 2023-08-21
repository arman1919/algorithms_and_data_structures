def removeDuplicates(nums:list[int]) -> int:
    new_arr = []
    for i in nums:
        if i not in new_arr:
            new_arr.append(i)
    lenn = len(new_arr)
    
    new_arr.extend((len(nums) - lenn - 1) * "_")
    
    nums[:] = new_arr[:]
    return lenn
            
            



nums = [0,0,1,1,1,2,2,3,3,4,4]

print(removeDuplicates(nums))

print(nums)

