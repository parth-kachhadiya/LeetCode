class Solution:
    def fib(self, n: int):
        c = 0
        a, b = 0, 1

        for _ in range(n):
            a, b = b, c
            c = a + b
        
        return c

print(Solution().fib(3))