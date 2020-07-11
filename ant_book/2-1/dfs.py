# 整数の入力
N = int(input())
# スペース区切りの整数の入力
A_list = [int(e) for e in input().split()]
# 整数の入力
K = int(input())

def dfs(I, SUM):
    if (I == N):
        return SUM == K
    if (dfs(I + 1, SUM)):
        return True
    if (dfs(I + 1, SUM + A_list[I])):
        return True
    return False

if (dfs(0,0)):
    print("Yes")
else:
    print("No")
