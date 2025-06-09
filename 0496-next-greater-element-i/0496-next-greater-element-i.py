class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Brute force: For each element in nums1, 
        find it in nums2, then look for next greater
        """
        result = []
        
        for num in nums1:
            # First, find where num is in nums2
            found_at = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    found_at = i
                    break
            
            # Then, look for next greater element after that position
            next_greater = -1
            for j in range(found_at + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break
            
            result.append(next_greater)
        
        return result