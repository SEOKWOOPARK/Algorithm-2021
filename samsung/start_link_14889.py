from itertools import combinations

n = int(input())
members = [i for i in range(n)] # 가능한 팀 조합을 만들기 위한 재료
s = [list(map(int, input().split())) for _ in range(n)]
possibleTeam = list(combinations(members, n // 2)) # 전체 인원을 두 그룹으로 나눈 조합 배열
gap = 10000 # 최솟값을 갱신할 초기 gap

for i in range(len(possibleTeam) // 2):
    team = possibleTeam[i] 
    A = 0 # 누적할 스텟값
    for j in range(n // 2):
        member = team[j] # 해당 조합 팀의 각 선수 설정
        for k in team: # 선수와 다른 선수 조합의 스탯 조회, 자기 자신과 스탯은 0
            A += s[member][k] # 스탯누적
    
    opposite = possibleTeam[-i-1] # 상대팀 마찬가지로 진행
    B = 0
    for j in range(n // 2):
        oppositeMember = opposite[j]
        for k in opposite:
            B += s[oppositeMember][k]
            
    gap = min(gap, abs(A - B)) # gap을 스탯값 차이와 비교
    
print(gap)