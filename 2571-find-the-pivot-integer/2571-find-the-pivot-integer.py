class Solution:
    def pivotInteger(self, n: int) -> int:
        # From the derivation, we know x^2 = (n^2 + n) / 2
        # Let's calculate the value that x^2 should be.
        target = (n * n + n) / 2
        
        # Take the square root to find a potential x.
        x = math.sqrt(target)
        
        # Check if x is a whole number. 
        # A simple way is to see if it has no fractional part.
        if x % 1 == 0:
            return int(x)
        else:
            return -1
