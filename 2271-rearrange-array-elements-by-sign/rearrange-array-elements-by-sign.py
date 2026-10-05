class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        pos = 0        # next even slot, for positives
        neg = 1        # next odd slot, for negatives
        for x in nums:
            if x > 0:
                result[pos] = x
                pos += 2
            else:
                result[neg] = x
                neg += 2
        return result
            
        