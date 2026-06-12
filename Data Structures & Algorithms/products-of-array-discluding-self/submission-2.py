class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate pre-fix array
        prefix = [1]
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            prefix.append(prod)
        
        postfix = []
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfix.append(prod)
        postfix.reverse()
        postfix.append(1)

        final_prod = []
        for i in range(len(nums)):
            final_prod.append(prefix[i] * postfix[i + 1])
        
        return final_prod


