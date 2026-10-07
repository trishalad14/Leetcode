class Solution(object):
    def minMoves2(self, nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]<key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        
        if n % 2 == 1:
         
            median=nums[n // 2]
        else:  
            median= (nums[n // 2 - 1] + nums[n // 2]) / 2
        total=0
        for x in nums:
            total+=abs(x-median)
        return total