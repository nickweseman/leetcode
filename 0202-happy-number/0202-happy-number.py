class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):
            total = 0
            while num > 0:
                total += (num % 10) ** 2
                num //= 10
            return total
        slow = fast = n
        while True:
            slow = happy(slow)
            fast = happy(happy(fast))
            if slow == fast:
                return slow == 1