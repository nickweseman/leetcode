class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0 # sum
        left = right = 0
        subarrays = 0

        while right < len(arr):
            window += arr[right]

            if right - left + 1 > k:
                window -= arr[left]
                left += 1
            if right - left + 1 == k and window / (right - left + 1) >= threshold :
                subarrays += 1
            right += 1
        return subarrays