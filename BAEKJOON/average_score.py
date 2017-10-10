# https://www.acmicpc.net/problem/10039

sumScore = 0
for n in range(5):

	score = int(raw_input())
	if score < 40 :
		score = 40

	sumScore += score

print sumScore / 5