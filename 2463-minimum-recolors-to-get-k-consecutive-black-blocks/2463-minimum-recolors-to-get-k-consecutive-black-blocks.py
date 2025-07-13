class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = 0
        whites = 0
        min_whites = math.inf
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

            