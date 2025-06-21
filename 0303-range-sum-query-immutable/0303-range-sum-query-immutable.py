class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sums = list(itertools.accumulate(nums, initial=0))
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]