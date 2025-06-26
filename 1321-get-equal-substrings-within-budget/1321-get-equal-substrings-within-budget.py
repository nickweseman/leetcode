class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = 0
        left = right = 0
        longest = -math.inf

        while right < len(s):
            cost += abs(ord(s[right]) - ord(t[right]))

            while left <= right and cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            if left <= right:
                longest = max(longest, right - left + 1)
            right += 1
        return 0 if longest == -math.inf else longest