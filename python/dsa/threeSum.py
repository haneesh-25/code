def threeSum(nums):
    nums.sort()
    ans = []
    arrLength = len(nums)
    for i in range(arrLength-2):
        ptr1 = i+1
        ptr2 = -1
        while ptr1+1!=arrLength+ptr2:
            if -nums[i]<nums[ptr1]+nums[ptr2]:
                ptr2 -= 1
            elif -nums[i]==nums[ptr1]+nums[ptr2]:
                ans.append([nums[i],nums[ptr1],nums[ptr2]])
                ptr1 = 0
                break
            else:
                ptr1+=1
        if -nums[i]==nums[ptr1]+nums[ptr2]:
            ans.append([nums[i],nums[ptr1],nums[ptr2]])
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))