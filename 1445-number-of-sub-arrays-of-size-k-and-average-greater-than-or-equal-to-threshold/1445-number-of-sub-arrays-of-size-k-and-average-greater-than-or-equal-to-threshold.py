class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarrays = 0
        left = right = 0
        threshold_total = threshold * k
        total = 0

        while right < len(arr):
            total += arr[right]

            if right - left + 1 > k:
                total -= arr[left]
                left += 1
            if right - left + 1 == k and total >= threshold_total:
                subarrays += 1
            right += 1
        return subarrays
