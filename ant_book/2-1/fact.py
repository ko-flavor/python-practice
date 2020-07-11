def fact(I):
    if I == 0:
        return 1
    return I*fact(I-1)

# 整数の入力
N = int(input())

print(fact(N))
