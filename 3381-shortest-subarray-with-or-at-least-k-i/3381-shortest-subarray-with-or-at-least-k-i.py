class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        MINIMUM WINDOW problem: Find shortest subarray with OR >= k
        Optimized for constraint: nums[i] <= 50, k < 64 (only need 6 bits)
        """
        left = 0
        right = 0
        n = len(nums)
        
        # Only need 6 bits since max value is 50 (and k < 64)
        bit_count = [0] * 6  # ← Changed from 32 to 6
        
        min_length = float('inf')
        
        def add(num):
            """Add num to window by updating bit frequencies"""
            for i in range(6):  # ← Changed from 32 to 6
                if num & (1 << i):
                    bit_count[i] += 1
        
        def remove(num):
            """Remove num from window by updating bit frequencies"""
            for i in range(6):  # ← Changed from 32 to 6
                if num & (1 << i):
                    bit_count[i] -= 1
        
        def get_current_or():
            """Calculate current OR from bit frequencies"""
            result = 0
            for i in range(6):  # ← Changed from 32 to 6
                if bit_count[i] > 0:
                    result |= (1 << i)
            return result
        
        while right < n:
            # Include nums[right] in window
            add(nums[right])
            
            # Shrink while window is still valid (OR >= k)
            while left <= right and get_current_or() >= k:
                # Update answer BEFORE shrinking
                min_length = min(min_length, right - left + 1)
                
                # Remove nums[left]
                remove(nums[left])
                left += 1
            
            right += 1
        
        return min_length if min_length != float('inf') else -1
        