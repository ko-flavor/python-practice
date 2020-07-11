# 整数の入力
N = int(input())
# スペース区切りの整数の入力
A_list = [int(e) for e in input().split()]

ANS = 0

for I in range(0,N):
    for J in range(I+1,N):
        for K in range(J+1,N):
            LEN = A_list[I]+A_list[J]+A_list[K]
            MAX = max(A_list[I],A_list[J],A_list[K])
            REST = LEN - MAX

            if REST > MAX:
              ANS = max(ANS,LEN)

print(ANS)
