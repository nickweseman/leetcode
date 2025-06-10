class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        NUM_BITS = 6
        bits = [0] * NUM_BITS
        left = right = 0
        shortest = float('inf')

        def add(n: int) -> None:
            for i in range(NUM_BITS):
                if n >> i & 1:
                    bits[i] += 1
        
        def remove(n: int) -> None:
            for i in range(NUM_BITS):
                if n >> i & 1:
                    bits[i] -= 1
        
        def windowValid() -> bool:
            total = 0
            for i in range(NUM_BITS):
                if bits[i]:
                    total |= 1 << i
            return total >= k
        
        def updateAnswer(left: int, right: int) -> None:
            nonlocal shortest
            shortest = min(shortest, right - left + 1)

        while right < len(nums):
            add(nums[right])

            while left <= right and windowValid():
                updateAnswer(left, right)
                remove(nums[left])
                left += 1
            print(f"{left=} {right=} {shortest=} {bits=}")
            right += 1
        return -1 if shortest == float('inf') else shortest

        