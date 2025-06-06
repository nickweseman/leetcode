class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        shortest = float('inf')
        left = right = 0

        NUM_BITS = 32
        bits = [0] * NUM_BITS

        def add(n: int):
            for i in range(NUM_BITS):
                if (n >> i) & 1:
                    bits[i] += 1
        
        def remove(n: int):
            for i in range(NUM_BITS):
                if (n >> i) & 1:
                    bits[i] -= 1
        
        def total_or():
            total = 0
            for i in range(NUM_BITS):
                if bits[i]:
                    total |= 1 << i
            return total

        while right < len(nums):
            add(nums[right])

            while left <= right and total_or() >= k:
                shortest = min(shortest, right - left + 1)
                remove(nums[left])
                left += 1
            right += 1
        return shortest if shortest != float('inf') else -1

