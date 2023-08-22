def findMin(nums: list[int]) -> int:
    
    l = len(nums) - 1
    mid = l // 2
    print(nums)
    if len(nums) == 1:
        return nums[0]
    
    if nums[-1] > nums[0]:
        return nums[l//2]
    findMin(nums[:mid])
    findMin(nums[mid:])
    
    

nums =  [3,4,5,1,2]
print(findMin(nums))