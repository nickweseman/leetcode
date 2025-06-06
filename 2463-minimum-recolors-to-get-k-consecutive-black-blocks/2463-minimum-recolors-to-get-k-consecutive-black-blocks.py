class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_whites = float('inf')
        window = 0
        left = right = 0

        while right < len(blocks):
            if blocks[right] == "W":
                window += 1
            
            if right - left + 1 > k:
                if blocks[left] == "W":
                    window -= 1
                left += 1
            
            if right - left + 1 == k:
                min_whites = min(min_whites, window)
            right += 1
        return min_whites
        