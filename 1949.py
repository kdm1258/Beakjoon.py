import sys
def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = weight[node]
    for child in tree[node]:
        if(child == parent):
            continue
        dfs(child, node)
        dp[node][0] += max(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]

n = int(input())
weight = list(map(int, sys.stdin.readline().split()))
weight.insert(0,0) #1index
tree = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1,-1)
print(max(max(dp)))