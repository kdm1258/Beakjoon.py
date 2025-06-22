import sys
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
res = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

def sol(r,c):
    #(1,1)의 경우
    if(r==0 and c==0):
        res[r-r1][c-c1] = 1
        return
    dim = max(abs(r),abs(c))
    start_val = (2*dim-1)**2+1
    base_r = dim-1 ; base_c = dim  
    if(r==c==dim):
        res[r-r1][c-c1] = (2*dim+1)**2
        return
    offset = base_r - r + base_c - c if r <=c else 8*dim-2-(base_r-r+base_c-c)
    res[r-r1][c-c1] = start_val + offset
    return

for i in range(r1,r2+1,1):
    for j in range(c1,c2+1,1):
        sol(i,j)


max_len = len(str(max(map(max, res))))
for row in res:
    print(" ".join(str(x).rjust(max_len) for x in row))
