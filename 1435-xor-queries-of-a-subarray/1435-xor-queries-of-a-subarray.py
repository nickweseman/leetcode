class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        result = []
        for left, right in queries:
            if left == 0:
                result.append(arr[right])
            else:
                result.append(arr[right] ^ arr[left - 1])
        return result
            