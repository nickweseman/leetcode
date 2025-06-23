class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = grand_sum = sum(nums)
        n = len(nums)
        answer = [0] * n

        for i in range(n):
            right_sum = grand_sum - left_sum
            left_sum += nums[i]
            answer[i] = abs(left_sum - right_sum)
        return answer
