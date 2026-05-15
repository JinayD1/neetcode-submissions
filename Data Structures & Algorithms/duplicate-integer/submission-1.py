class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if seen.get(num, 0) != 0:
                return True
            else:
                seen[num] = seen.get(num, 0) + 1
        return False