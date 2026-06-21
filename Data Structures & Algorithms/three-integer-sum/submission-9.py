class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            # Since the array is sorted, no triplet can sum to 0 after this.
            if nums[i] > 0:
                break

            # Skip duplicate target values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                total = nums[i] + nums[p1] + nums[p2]

                if total < 0:
                    p1 += 1

                elif total > 0:
                    p2 -= 1

                else:
                    triplets.append([nums[i], nums[p1], nums[p2]])

                    p1 += 1
                    p2 -= 1

                    # Skip duplicate left values.
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1

                    # Skip duplicate right values.
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1

        return triplets