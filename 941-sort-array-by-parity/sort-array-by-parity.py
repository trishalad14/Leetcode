class Solution(object):
    def sortArrayByParity(self, nums):
        n=len(nums)
        for i in range(n-1):
            swapped=False
            for j in range(n-1-i):
                if nums[j]%2!=0:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped=True
            if swapped==False:
                break
        return nums

        