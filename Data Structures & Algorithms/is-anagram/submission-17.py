class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char_map.get(char, 0) == 0:
                return False
            else:
                char_map[char] = char_map.get(char, 0) - 1
        
        return True