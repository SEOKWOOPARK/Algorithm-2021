import sys

def getDecimal(num, decimalNums, digit = 1):
	if digit > 10: 
		# digit은 자릿수. 1 ~ 9까지 자릿수만큼만 가능
		# 1자리, 2자리, 3자리 ∙∙∙ 9자리
		return
	
	decimalNums(num) # 감소하는 수 모으기

	for i in range(10):
		if (num % 10) > i: 
			getDecimal((num * 10) + i, decimalNums, digit = digit + 1)
			# '%' 연산 => 해당 num과 i(0 ~ 9 숫자들)을 대소 비교하는 장치
			# i가 num 보다 작으면 num을 i보다 한자리 올리기 위해 (num * 10) + i
			# 감소하는 수를 발견하면 digit(자릿수)를 하나 늘려 DFS로 쭉 들어간다.
	return decimalNums

input = sys.stdin.readline
n = int(input()) 
decimalNums = [] # 감소하는 수를 싹 집어넣을 배열

for num in range(10):
	r = getDecimal(num, decimalNums)

r.sort()

if n >= 1023:
	print(-1)
else:
	print(r[n]) # 인덱스 1번부터 18번째이므로 r[n] 출력

