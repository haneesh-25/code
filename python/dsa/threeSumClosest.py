def threeSumClosest(nums,target):
    nums.sort()
    ans = 0
    for i,a in enumerate(nums):
        if i>0 and a == nums[i-1]:
            continue
        l,r = i+1,len(nums)-1
        while l<r:
            threesum = a+nums[l]+nums[r]
            if ans == 0:
                ans = threesum
            if abs(target-threesum) < abs(ans-threesum):
                ans = threesum
            if(threesum>target):
                r-=1
            elif(threesum<target):
                l+=1
            else:
                ans = target
                return ans
    return ans

target= 100
nums = [1,1,1,0]
threeSumClosest(nums,target)