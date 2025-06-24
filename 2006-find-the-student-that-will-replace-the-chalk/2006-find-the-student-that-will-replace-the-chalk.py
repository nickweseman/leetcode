class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        left_sum, right_sum = 0, sum(chalk)

        k %= right_sum

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]