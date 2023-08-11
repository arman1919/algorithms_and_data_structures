class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lenn = len(nums)
        
        for i in range(lenn):
            for j in range(lenn):
                if nums[i]+nums[j] == target and i != j:
                    ls = []
                    return i,j
        
    



s = Solution()
ls = [1,2,3,4,5,6]
print(s.twoSum(ls,7))
ls = [3,2,4]
print(s.twoSum(ls,6))




