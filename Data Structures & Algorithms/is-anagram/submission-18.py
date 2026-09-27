class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for char in s:
            smap[char] = smap.get(char, 0) + 1

        for char in t:
            if smap.get(char, 0) == 0:
                return False
            else:
                smap[char] = smap[char] - 1
        
        return True
        