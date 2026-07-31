class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t): return False
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        for c in t:
            if seen.get(c, 0) == 0:
                return False
            seen[c] = seen.get(c, 0) - 1
        return True