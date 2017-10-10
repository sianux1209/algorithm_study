#https://www.acmicpc.net/problem/2675

T = raw_input()

for case in range(int(T)):

	li = []

	R, S = raw_input().split()

	for alpha in S:
		li.append(alpha*int(R))
	print ''.join(li)
