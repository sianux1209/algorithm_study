# https://www.acmicpc.net/problem/11866
# https://www.acmicpc.net/submit/1158

N, M = map(int, raw_input().split())

people = [people for people in range(1, N+1)]

index = 0
result = []

for choise in range(N):

	index +=M
	if index % len(people) == 0:
		index = len(people)
	else:
		index %= len(people)

	result.append(people.pop(index-1))
	index-=1


	#print people, "\t\t\t", result, "\t", index

print "<" + ", ".join(map(str, result)) + ">"