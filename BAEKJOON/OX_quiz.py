# https://www.acmicpc.net/problem/8958

T = raw_input()

for testCase in range(int(T)):

	input = raw_input()

	userScore = 0
	scoreCount = 1
	
	for question in input:

		if question == 'O':
			userScore +=scoreCount
			scoreCount+=1

		else :
			scoreCount = 1

	print userScore