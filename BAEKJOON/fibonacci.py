# https://www.acmicpc.net/problem/2747

def fibonacci(num):
	a, b = 0, 1

	for i in range(num):
		a, b = b, a+b

	return a

print fibonacci(int(raw_input()))