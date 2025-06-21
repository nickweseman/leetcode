class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        min_whites = float('inf')
        left = right = 0

        while right < len(blocks):
            if blocks[right] == "W":
                whites += 1
            if right - left + 1 > k:
                if blocks[left] == "W":
                    whites -= 1
                left += 1
            if right - left + 1 == k:
                min_whites = min(min_whites, whites)
            right += 1
        return min_whites