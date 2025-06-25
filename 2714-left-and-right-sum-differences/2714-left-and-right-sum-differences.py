class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        answer = []

        for i, num in enumerate(nums):
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
        return answer

