class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 != p2:
            sumt = numbers[p1] + numbers[p2]
            if sumt > target:
                p2 -= 1
            elif sumt < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]