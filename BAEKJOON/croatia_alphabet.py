# https://www.acmicpc.net/problem/2941

input = raw_input()

count = 0

for alpha in li:
	count += input.count(alpha)
	input = input.replace(alpha,"")

print count + len(input)