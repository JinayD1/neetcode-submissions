class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # step 1: sliding approach
        # valid: len - count of largest <= k
        charmap = {}
        sub = []
        l, largest = 0, 0

        maxlen = 0

        for r in range(len(s)):
            charmap[s[r]] = charmap.get(s[r], 0) + 1
            largest = max(charmap.values())
            while(r - l + 1 - largest > k):
                charmap[s[l]] -= 1
                l += 1
                largest = max(charmap.values())
            maxlen = max(r - l + 1, maxlen)
    
        return maxlen

        

            
        