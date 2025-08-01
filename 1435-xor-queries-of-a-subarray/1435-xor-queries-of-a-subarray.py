class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        return result