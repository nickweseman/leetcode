class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        shortest = float('inf')
        NUM_BITS = 6
        bits = [0] * NUM_BITS

        def add() -> None:
            for i in range(NUM_BITS):
                if nums[right] >> i & 1:
                    bits[i] += 1
        def remove() -> None:
            for i in range(NUM_BITS):
                if nums[left] >> i & 1:
                    bits[i] -= 1
        def total_or() -> int:
            total = 0
            for i in range(NUM_BITS):
                if bits[i]:
                    total |= 1 << i
            return total
        while right < len(nums):
            add()
            while left <= right and total_or() >= k:
                shortest = min(shortest, right - left + 1)
                remove()
                left += 1
            right += 1
        return -1 if shortest == float('inf') else shortest