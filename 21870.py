import sys
import math

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)  # 1-indexing

def solve(l, r):
    if l == r:
        return arr[l]

    m = (l + r - 1) // 2

    # 왼쪽 구간 GCD 구하기 (왼쪽 먼저 선택)
    left_gcd = arr[l]
    for i in range(l+1, m+1):
        left_gcd = math.gcd(left_gcd, arr[i])
    left_res = left_gcd + solve(m+1, r)

    # 오른쪽 구간 GCD 구하기 (오른쪽 먼저 선택)
    right_gcd = arr[m+1]
    for i in range(m+2, r+1):
        right_gcd = math.gcd(right_gcd, arr[i])
    right_res = right_gcd + solve(l, m)

    return max(left_res, right_res)

print(solve(1, n))
