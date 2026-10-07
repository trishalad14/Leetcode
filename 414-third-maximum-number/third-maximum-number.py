class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        n = len(nums)

        if n < 3:
            return max(nums)

        for i in range(3):
            max_idx = i
            for j in range(i + 1, n):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

        return nums[2]