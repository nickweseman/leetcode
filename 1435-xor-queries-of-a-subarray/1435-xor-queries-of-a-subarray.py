class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []

        prefix_xor = [0]
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
        
        for left, right in queries:
            #left, right = q
            answer.append(prefix_xor[right + 1] ^ prefix_xor[left])
        return answer