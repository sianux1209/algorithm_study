#https://www.acmicpc.net/problem/1316

T = raw_input()

result = 0
for case in range(int(T)):

	input = raw_input()

	blackList = []

	flag = True
	privious = ''
	for alpha in input:
		if alpha not in blackList:
			blackList.append(alpha)
			#print blackList

		elif privious == alpha:
			continue

		else:
			flag = False

		privious = alpha

	if flag == True:
		result +=1

print result