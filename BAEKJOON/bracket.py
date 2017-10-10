# https://www.acmicpc.net/problem/9012

T = raw_input()

for caseCount in range(int(T)):

	bracket = raw_input()

	openCnt = 0

	for char in bracket:
		if char == "(":
			openCnt += 1

		else:
			openCnt -= 1

		# if a lot of close more then open
		if openCnt < 0:
			break

	if openCnt == 0:
		print "YES"
	else:
		print "NO"