# 整数の入力
L = int(input())
# 整数の入力
N = int(input())
# スペース区切りの整数の入力
X_list = [int(e) for e in input().split()]

MIN = 0
MAX = 0
for I in range(N):
    MIN = max(MIN,min(X_list[I],L-X_list[I]))
    MAX = max(MAX,max(X_list[I],L-X_list[I]))
print(MIN)
print(MAX)
