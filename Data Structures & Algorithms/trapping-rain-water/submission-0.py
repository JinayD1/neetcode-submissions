class Solution:
    def trap(self, height: List[int]) -> int:
        # water stored each cell iven by min(L, R) - curr height
        # use prefix sum for left max, right max and min(L, R) at each
        # then calculate water at each cell, while 
        # adding up continuous and keeping max track
        n = len(height)
        maxl = [0] * n
        maxr = [0] * n
        minmax = [0] * n
        maxw = 0

        for i in range(1, n):
            maxl[i] = max(maxl[i - 1], height[i - 1])

        for j in range(n - 2, 0, -1):
            maxr[j] = max(maxr[j + 1], height[j + 1])

        for k in range(n):
            minmax[k] = min(maxl[k], maxr[k])
        
        for g in range(n):
            wcell = minmax[g] - height[g]
            if wcell > 0:
                maxw += wcell
        
        return maxw
        


