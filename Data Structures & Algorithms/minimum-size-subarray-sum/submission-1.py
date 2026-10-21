class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minlen = len(nums) + 1
        sumcurr = 0

        for r in range(len(nums)):
            sumcurr += nums[r]
            while (sumcurr >= target):
                minlen = min(minlen, r - l + 1)
                sumcurr -= nums[l]
                l += 1     

        if (minlen > len(nums)):
            return 0
        else:
            return minlen