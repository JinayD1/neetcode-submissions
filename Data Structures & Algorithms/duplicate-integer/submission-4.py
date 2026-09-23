class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for num in nums:
            if keys.get(num, 0) != 0:
                return True
            else:
                keys[num] = 1
        return False