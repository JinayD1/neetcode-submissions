class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k - 1
        minarr = []

        # (nums[l] - target + nums[r] - target)
        # as low as possible
        closeness = 100000
        
        while(r < len(arr)):
            curr = 0
            currarr = []
            for i in range(l, r + 1):
                curr += abs(arr[i] - x)
                currarr.append(arr[i])
            if (closeness > curr):
                closeness = curr
                minarr = arr[l: r + 1]
            r += 1
            l += 1
        return minarr