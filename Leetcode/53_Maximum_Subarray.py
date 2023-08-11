# incomplete solution

import math

def maxSubArray(nums: list[int]) -> int:
    lenght = len(nums)
    
    sub_arrs = -math.inf 
      
    for i in range(lenght):
        for j in range(i,lenght):
            
            
            if sum(nums[i:j+1]) >= sub_arrs:
                sub_arrs = sum(nums[i:j+1])

            
        
    return sub_arrs

    
nums = [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1,-93,42,44,1]


print(maxSubArray(nums))
