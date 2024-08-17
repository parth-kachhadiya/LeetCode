class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        else:
            a, b, c, d = 0, 1, 1, 0
            for _ in range(2,n):
                d = a + b + c
                if _ == (n-1):
                    return d
                a, b, c = b, c, d

print(Solution().tribonacci(25)) 
