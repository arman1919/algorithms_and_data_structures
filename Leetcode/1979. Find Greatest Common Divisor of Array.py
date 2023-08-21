def findGCD(nums: list[int]) -> int:
    min_ = nums[0]
    max_ = nums[0]
    
    for i in nums:
        if i > max_:
            max_ = i
        if i < min_:
           min_ = i
   
    for i in range(min_+1,-1,-1):
        if min_ % i == 0 and max_ % i == 0:
            return i


       
nums = [7,5,6,8,3]
print(findGCD(nums))
