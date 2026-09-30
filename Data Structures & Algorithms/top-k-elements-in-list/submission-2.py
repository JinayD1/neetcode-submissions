class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create count map of nmbers
        countmap = {}
        for num in nums:
            countmap[num] = countmap.get(num, 0) + 1

        # use buckets as count values of each item
        # learn this syntax
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in countmap.items():
            buckets[c].append(n)
        
        res = []
        for i in reversed(range(len(buckets))):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res