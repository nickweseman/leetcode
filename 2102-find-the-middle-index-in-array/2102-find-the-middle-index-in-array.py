class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sums = list(itertools.accumulate(nums, initial=0))

        for i in range(len(nums)):
            if prefix_sums[i] == prefix_sums[-1] - prefix_sums[i + 1]:
                return i
        return -1