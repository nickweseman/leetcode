class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        for q in queries:
            left, right = 0, len(prefix_sum)

            while left < right:
                mid = (left + right) // 2

                if prefix_sum[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
            answer.append(left - 1)
        return answer