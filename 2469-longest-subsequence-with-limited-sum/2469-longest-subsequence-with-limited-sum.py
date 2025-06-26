class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        for q in queries:
            left, right = 0, len(prefix_sum)

            while left < right:
                mid = (left + right) // 2

                if prefix_sum[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
            answer.append(left)
        return answer