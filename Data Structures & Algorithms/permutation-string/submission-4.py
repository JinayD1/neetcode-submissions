class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed-size sliding window
        l, r = 0, len(s1) - 1

        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1
        
        winmap = {}
        for char in s2[l: r]:
            winmap[char] = winmap.get(char, 0) + 1
        
        while (r < len(s2)):
            winmap[s2[r]] = winmap.get(s2[r], 0) + 1
            if s1map == winmap:
                return True
            winmap[s2[l]] = winmap.get(s2[l], 0) - 1 
            if winmap.get(s2[l], 0) == 0:
                del winmap[s2[l]]
            l += 1
            r += 1
        
        return False