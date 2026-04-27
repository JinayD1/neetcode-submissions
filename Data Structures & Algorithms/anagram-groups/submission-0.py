class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        seen = {}
        for c in s:
            # use get to default to 0, if no key is found 
            seen[c] = seen.get(c, 0) + 1

        for c in t:
            if (seen.get(c, None) == None or seen.get(c, None) == 0):
                return False
            else:
                seen[c] -= 1
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        added = []
        combos = {}
        for i in range(len(strs)):
            if i in added:
                continue
            combos[strs[i]] = [strs[i]];
            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    combos[strs[i]].append(strs[j])
                    added.append(j)
        
        final = []
        for combo in combos.values():
            final.append(combo)

        return final