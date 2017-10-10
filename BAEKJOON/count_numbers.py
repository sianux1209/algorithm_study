# https://www.acmicpc.net/problem/2577

A = int(raw_input())
B = int(raw_input())
C = int(raw_input())

result = str(A*B*C)

numbers = {}

for number in range(0, 10):
	numbers[number] = 0

for number in result:
	numbers[int(number)] = numbers[int(number)] + 1

for number in numbers.values():
	print number