class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}
        for num in nums:
            if track.get(num, 0) >= 1:
                return True
            else:
                track[num] = track.get(num, 0) + 1
        return False