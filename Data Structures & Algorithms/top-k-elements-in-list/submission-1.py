class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        # array of empty arrays of length of nums
        bsort = [[] for i in range(len(nums) + 1)] 
        topK = []

        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
        
        for num, freq in numMap.items():
            bsort[freq].append(num)
        
        # iterate through the list index in reverse.
        for nums in reversed(bsort):
            for n in nums:
                topK.append(n)
                if len(topK) == k:
                    return topK