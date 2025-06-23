class Solution:
    def pivotInteger(self, n: int) -> int:
        # x^2 = (n^2 + n) / 2
        target = (n ** 2 + n) / 2
        x = math.sqrt(target)
        
        # Check if x is a whole number. 
        if x == int(x):
            return int(x)
        else:
            return -1
