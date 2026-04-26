class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if seen.get(target - nums[i], None) != None:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i