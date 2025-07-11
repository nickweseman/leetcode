class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        shortest = math.inf
        NUM_BITS = 8
        bits = [0] * NUM_BITS
        left = right = 0
        def add():
            for i in reversed(range(NUM_BITS)):
                if (nums[right] >> i) & 1:
                    bits[i] += 1
        def remove():
            for i in reversed(range(NUM_BITS)):
                if (nums[left] >> i) & 1:
                    bits[i] -= 1
        def at_least_k():
            total = 0
            for i in range(NUM_BITS):
                if bits[i]:
                    total += 1 << i
            return total >= k

        while right < len(nums):
            add()
            while left <= right and at_least_k():
                shortest = min(shortest, right - left + 1)
                remove()
                left += 1
            right += 1
        return -1 if shortest == math.inf else shortest