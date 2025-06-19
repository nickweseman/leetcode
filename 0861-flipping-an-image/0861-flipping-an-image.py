class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            result.append(list(reversed(row)))
        for row in result:
            for j in range(len(row)):
                row[j] ^= 1
        return result