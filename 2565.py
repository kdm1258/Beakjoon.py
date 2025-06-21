import sys
n = int(sys.stdin.readline())
lines = []
dp = [1]*n

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lines.append((a,b))

lines.sort()

for i in range(len(lines)):
    for j in range(i):
        if(lines[i][1] > lines[j][1]):
            dp[i] = max(dp[i], dp[j]+1)

print(n-dp[n-1])