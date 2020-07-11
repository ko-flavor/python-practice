def fib(I):
    if I == 0 or I == 1:
        return 1
    return fib(I-1)+fib(I-2)

# 整数の入力
N = int(input())

for I in range(0,N):
    print(fib(I))
