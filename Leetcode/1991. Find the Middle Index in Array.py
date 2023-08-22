def findMiddleIndex(nums: list[int]) -> int:
    
        totalSum = 0
        for i in nums:
            totalSum += i
        
        leftSum = 0
        
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        
        return -1
    
    
            
        

nums =  [-3,-3,15]

print(findMiddleIndex(nums))