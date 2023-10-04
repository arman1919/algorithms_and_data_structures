def foo (nums:list,p):
    
    l = len(nums)
    i = 0
    
    for _ in range(l):
        
        if nums[i] > p:
            tmp = nums[i]
            nums.pop(i)
            nums.append(tmp)
            
        elif nums[i] == p:
            i += 1
            
        else:
            
            tmp = nums[i]
            nums.pop(i)
            nums.insert(0,tmp)
            i +=1


nums = [6,9,8,4,3,6,5,7,1,4,6,9]

foo(nums,4)

print(nums)

