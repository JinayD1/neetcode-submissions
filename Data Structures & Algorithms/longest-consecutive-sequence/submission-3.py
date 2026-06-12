class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        fseq = []
        pseq = []
        for num in nums:
            if not pseq:
                pseq.append(num)
            elif pseq[-1] == num:
                continue
            elif pseq[-1] == num - 1:
                pseq.append(num)
            else:
                if len(pseq) > len(fseq):
                    fseq = pseq.copy()
                pseq = [num]
        if len(pseq) > len(fseq):
            fseq = pseq.copy()
        return len(fseq)
            
        
