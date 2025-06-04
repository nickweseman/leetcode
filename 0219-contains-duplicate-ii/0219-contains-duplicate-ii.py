from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        window = defaultdict(int)

        while right < len(nums):
            right_element = nums[right]
            window[right_element] += 1

            while right - left > k:
                left_element = nums[left]
                window[left_element] -= 1

                if window[left_element] == 0:
                    del window[left_element]
                
                left += 1
            
            if window[right_element] > 1:
                return True
            right += 1
        return False
        