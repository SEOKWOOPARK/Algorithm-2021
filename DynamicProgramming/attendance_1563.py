import sys
sys.setrecursionlimit(10**6)

N = int(input())
dp=[[[-1 for absent in range(3)] for late in range(2)] for day in range(N + 1)]

# 역방향 DP => 가장 마지막 깊이(day4)부터 누적해서 day 1까지 만든다 
def dfs(day, late, absent):
    if (late == 2) or (absent == 3): # 지각 2번 or 결석연속 3번
        return 0

    if day == N:
        return 1

    if dp[day][late][absent] == -1: # 참석 + 지각 + 결석
        attend = dfs(day + 1, late, 0) + dfs(day + 1, late + 1, 0) + dfs(day + 1, late, absent + 1)
        dp[day][late][absent] = attend
        return attend
    else:
        return dp[day][late][absent]
            
print((dfs(0, 0, 0)) % 1000000)