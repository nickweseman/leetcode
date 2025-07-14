class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for row in image:
            new_image.append(row[::-1])
        for i, row in enumerate(new_image):
            for j, pixel in enumerate(row):
                new_image[i][j] ^= 1
        return new_image