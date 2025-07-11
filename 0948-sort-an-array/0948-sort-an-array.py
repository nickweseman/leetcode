class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        MIN_VAL, MAX_VAL = -50_000, 50_000
        offset = -MIN_VAL
        size = MAX_VAL - MIN_VAL + 1
        counts = [0] * size
        for num in nums:
            counts[num + offset] += 1
        index = 0
        for i, freq in enumerate(counts):
            for _ in range(freq):
                nums[index] = i - offset
                index += 1
        return nums 

        