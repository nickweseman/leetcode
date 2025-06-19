class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(x: int) -> int:
            total = 0

            while x:
                total += (x % 10) ** 2
                x //= 10
            return total
        
        fast = slow = happy(n)

        while True:
            slow = happy(slow)
            fast = happy(happy(fast))

            if slow == fast:
                return slow == 1
