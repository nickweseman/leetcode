class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        result = []
        for num1, freq1 in counter1.items():
            if num1 in counter2:
                result.extend([num1] * min(freq1, counter2[num1]))
        return result