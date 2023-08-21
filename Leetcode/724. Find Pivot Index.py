def pivotIndex(nums: list[int]) -> int:
    for i in range(len(nums)):
        if  sum(nums[:i+1]) == sum(nums[i:]):
            return i

    return -1


nums = [1,7,3,6,5,6]

print(pivotIndex(nums))
