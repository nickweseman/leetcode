class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        NUM_BITS = 32
        bits = [0] * 32
        min_length = float('inf')

        def add(num: int) -> None:
            for i in range(NUM_BITS):
                if (num >> i) & 1:
                    bits[i] += 1
        
        def remove(num: int) -> None:
            for i in range(NUM_BITS):
                if (num >> i) & 1:
                    bits[i] -= 1
        
        def total_or(num: int) -> bool:
            result = 0
            for i in range(NUM_BITS):
                if bits[i] >= 1:
                    result |= 1 << i
            return result
        
        while right < len(nums):
            add(nums[right])

            while left <= right and total_or(nums[left]) >= k:
                min_length = min(min_length, right - left + 1)

                remove(nums[left])
                left += 1
            right += 1
        return min_length if min_length != float('inf') else -1