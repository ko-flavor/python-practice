import bisect

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False

# 整数の入力
N = int(input())
# 整数の入力
M = int(input())
# スペース区切りの整数の入力
K_list = [int(e) for e in input().split()]

K_list.sort()

f = False

for I in range(0,N):
    for J in range(0,N):
        for K in range(0,N):
            if index(K_list,M-K_list[I]-K_list[J]-K_list[K]):
                f = True
                
print("OK" if f else "NG")
