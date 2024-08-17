def tribonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(0, 1, 1)
    else:
        a, b, c, d = 0, 1, 1, 0
        print(f'{a}, {b}, {c}',end=", ")
        for _ in range(3,n+1):
            d = a + b + c
            print(d,end=", ")
            a, b, c = b, c, d

def tribonacci_2(n):
    if n <= 2:
        return 0 if n == 0 else 1
    else:
        a, b, c, d = 0, 1, 1, 0
        for _ in range(2,n):
            d = a + b + c
            if _ == (n-1):
                return d
            a, b, c = b, c, d

print(tribonacci_2(25)) 