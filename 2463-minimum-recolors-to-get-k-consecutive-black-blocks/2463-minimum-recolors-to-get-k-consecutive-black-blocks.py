class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        left = right = 0
        min_operations = float('inf')

        while right < len(blocks):
            if blocks[right] == "W":
                whites += 1
            
            if right - left + 1 > k:
                if blocks[left] == "W":
                    whites -= 1
                left += 1
            if right - left + 1 == k:
                min_operations = min(min_operations, whites)
            right += 1
        return min_operations