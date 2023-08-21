def findMiddleIndex(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    if len(nums) == 2 and nums[0] > nums[1]:
        return 0
    summ = nums[0] + nums[1]   
    for i in range(2,len(nums)):
        if  i == len(nums)-1 and summ + nums[i] < summ:
            summ += nums[i]
            return summ
        
        if summ + nums[i] >= summ:
            return i
        else:
            summ += nums[i]
            
        
    return -1
    
    


nums =  [2,-3]

print(findMiddleIndex(nums))