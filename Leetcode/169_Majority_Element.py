def majorityElement(nums: list[int]) -> int:
    counts = {}
    max_count = 0
    major = nums[0]
    for i in nums:
        if i in counts:
            
            counts[i] += 1
            if counts[i] > max_count:
                max_count = counts[i]
                major = i   
        else:
            counts[i] = 1        

    return major


nums = [2,2,1,1,1,2,3,3,3,3,3,3,3,3,2]


print(majorityElement(nums))