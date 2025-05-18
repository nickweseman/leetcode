class Solution:
    def isHappy(self, n: int) -> bool:
        def f(n: int):
            output = 0

            while n:
                output += (n % 10) ** 2    
                n = n // 10

            return output
        
        slow = f(n)
        fast = f(f(n))

        while f(n) and f(f(n)):
            if fast == slow:
                return slow == 1 or fast == 1

            slow = f(slow)
            fast = f(f(fast))
                   
        return slow == 1 or fast == 1


    
        