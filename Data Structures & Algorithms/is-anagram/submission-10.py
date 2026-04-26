class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = {}

        # load all characters of s into the dictionary
        # store the count of each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # get if s count is in t
        for ch in t:
            if count.get(ch, None) == 0 or count.get(ch, None) == None:
                return False
            count[ch] = count.get(ch, None) - 1
        return True