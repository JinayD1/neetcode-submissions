class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allprod = []
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    allprod = [0] * len(nums)
                    allprod[i] = prod
                    return allprod
                else:
                    allprod.append(int(prod / nums[i]))
        return allprod

