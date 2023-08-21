def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0  
    count = 1  
    for fast in range(1, len(nums)):
    
        if nums[fast] == nums[slow]:         
            count += 1
            if count <= 2:
                slow += 1
                nums[slow] = nums[fast]
                           
        else:  
            count = 1
            slow += 1
            nums[slow] = nums[fast]
            

    return slow + 1
