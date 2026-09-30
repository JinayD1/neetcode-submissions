class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hash-map storing occurences of each element
        # find min of each, then subtract
        # find largest difference between
        count = defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
        
        for num, indices in count.items():
            if len(indices) >= 2:
                l, r = 0, 1
                while (r < len(indices)):
                    diff = abs(indices[l] - indices[r])
                    if diff <= k:
                        return True
                    l += 1
                    r += 1
        
        return False