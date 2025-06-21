class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sums = list(itertools.accumulate(nums))
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]