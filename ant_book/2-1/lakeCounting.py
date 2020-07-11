# 整数の入力
N = int(input())
# 整数の入力
M = int(input())
# 池の情報の入力
Lake = [0 for j in range(N)]
for I in range(0,N):
    Lake[I]=list(input())

def dfs(X,Y):
    Lake[X][Y]="."
    for I in range(-1,2):
        for J in range(-1,2):
            NX = X + I
            NY = Y + J
            if(0 <= NX and NX < N and 0<= NY and NY < M and Lake[NX][NY] == "W"):
                dfs(NX,NY)

RES = 0
for I in range(0,N):
    for J in range(0,M):
        if (Lake[I][J] == "W"):
            dfs(I,J)
            RES+=1

print(Lake)
print(RES)
