class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary value with list as the value
        anagroups = defaultdict(list)
        for word in strs:
            wmap = [0] * 26
            for c in word:
                wmap[ord(c) - ord('a')] += 1
            maptuple = tuple(wmap)
            anagroups[maptuple].append(word)
        res = []
        for group in anagroups:
            res.append(anagroups[group])
        return res


                
