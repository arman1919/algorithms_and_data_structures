
def searchRange(nums: list[int], target: int) -> list[int]:
    if target not in nums or len(nums) == 0:
            
        return [-1,-1]
    
    start = nums.index(target)
    stop  = start
    while stop < len(nums)-1 and len (nums) != 1:
        
        if nums[stop+1] == target:
            stop += 1 
        else:
            break
        
    return start,stop
             








nums = [1,1,1,1,1]

print(searchRange(nums,5))

