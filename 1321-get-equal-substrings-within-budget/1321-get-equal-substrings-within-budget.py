class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        window = 0
        left = right = 0
        max_length = 0

        while right < len(s):
            window += abs(ord(s[right]) - ord(t[right]))

            while window > maxCost:
                window -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
        