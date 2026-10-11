class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        sub = set()
        maxlen = 0
        
        l, r = 0, 0
        while (r < len(s)):
            while (r < len(s) and s[r] not in sub):
                sub.add(s[r])
                r += 1
            maxlen = max(maxlen, len(sub))
            sub.remove(s[l])
            l += 1
        
        return maxlen