class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return False
        pairs = {')': '(', ']': '[', '}': '{'}

        stack = []
        for c in s:
            if c in list(pairs.values()):
                stack.append(c)
            elif len(stack) == 0 or stack[-1] != pairs[c]: 
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0
                