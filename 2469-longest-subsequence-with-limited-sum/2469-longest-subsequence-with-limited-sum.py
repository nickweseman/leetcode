class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1,len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        print(locals())
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