class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = k * threshold
        subarrays = 0
        left = right = 0
        total = 0

        while right < len(arr):
            total += arr[right]

            if right - left + 1 > k:
                total -= arr[left]
                left += 1
            if right - left + 1 == k and total >= threshold:
                subarrays += 1
            right += 1
        return subarrays