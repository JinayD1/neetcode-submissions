class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub = set()
        maxlen = 0

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            maxlen = max(maxlen, len(sub))
            r += 1
        
        return maxlen