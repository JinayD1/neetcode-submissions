class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapNums = {}
        results = []
        topK = []

        for num in nums:
            mapNums[num] = mapNums.get(num, 0) + 1

        for num, freq in mapNums.items():
            results.append([freq, num])
        
        results.sort(reverse=True)
        for i in range(k):
            topK.append(results[i][1])

        return topK

            
