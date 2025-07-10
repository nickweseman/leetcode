class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        MIN_VAL, MAX_VAL = -50_000, 50_000
        count_size = MAX_VAL - MIN_VAL + 1
        offset = -MIN_VAL
        counts = [0] * count_size
        for num in nums:
            counts[num + offset] += 1 # shifts the range from [-50k, 50k] to [0, 100k] for array indexing
        index = 0
        for i in range(count_size):
            for _ in range(counts[i]):
                nums[index] = i - offset # shifts back from [0, 100k] to [-50k, 50k] for the actual values
                index += 1
        return nums