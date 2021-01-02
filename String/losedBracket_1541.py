list = input().split('-')
total = 0

for i in list[0].split('+'):
	total += int(i)

for i in list[1:]:
	for j in i.split('+'):
		total -= int(j)

print(total)