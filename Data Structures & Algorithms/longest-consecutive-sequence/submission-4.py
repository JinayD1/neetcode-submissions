class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            seq = []
            if (num - 1) not in numset:
                seq.append(num)
                while seq[-1] in numset:
                    if seq[-1] + 1 in numset:
                        seq.append(seq[-1] + 1)
                    else:
                        break
                if len(seq) > longest:
                    longest = len(seq)
        return longest

        
