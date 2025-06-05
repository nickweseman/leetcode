class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        right = 0
        
        # Technically only need 6 bits since nums[i] <= 50 (50 in binary = 110010 (6 bits)) and k < 64 (63 = 111111 (6 bits))
        bit_count = [0] * 32
        
        min_length = float('inf')
        
        def add(num):
            for i in range(6):
                if (num >> i) & 1:
                    bit_count[i] += 1

        def remove(num):
            for i in range(6):
                if (num >> i) & 1:
                    bit_count[i] -= 1

        def get_current_or():
            result = 0
            for i in range(6):
                if bit_count[i] > 0:
                    result |= (1 << i) 
            return result
        
        while right < len(nums):
            add(nums[right])
            
            # Shrink while window is still valid (OR >= k)
            while left <= right and get_current_or() >= k:
                # Update answer BEFORE shrinking
                min_length = min(min_length, right - left + 1)
                
                remove(nums[left])
                left += 1
            right += 1
        
        return min_length if min_length != float('inf') else -1
        