class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []

        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1] 
        
        for left, right in queries:
            if left == 0:
                answer.append(arr[right])
            else:
                answer.append(arr[right] ^ arr[left - 1])
        return answer