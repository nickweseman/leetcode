class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = -math.inf
        left = right = 0
        cost = 0
        while right < len(s) and right < len(t):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length