class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key (target - num, index of num)
        seen = {}
        for index in range(len(nums)):
            if nums[index] in seen:
                return [seen[nums[index]], index]
            else:
                seen[target - nums[index]] = index 