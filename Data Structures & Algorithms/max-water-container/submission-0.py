class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # converging pointer technique
        b1 = 0
        b2 = len(heights) - 1
        maxarea = 0

        while b1 != b2:
            area = min(heights[b1], heights[b2]) * (b2 - b1)
            if area > maxarea:
                maxarea = area
            if heights[b1] < heights[b2]:
                b1 += 1
            else:
                b2 -= 1
            
        return maxarea

