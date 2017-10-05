# https://www.acmicpc.net/problem/2941

class Stack:

	stack = []

	def push(self, var):
		self.stack.append(var)

	def pop(self):
		if self.size() != 0:
			return self.stack.pop()
		else:
			return -1

	def size(self):
		return len(self.stack)

	def empty(self):
		if self.size() == 0:
			return 1
		else:
			return 0

	def top(self):
		if self.empty() == 1:
			return -1
		else:
			return self.stack[-1]


if __name__ == "__main__":

	stack = Stack()

	N = raw_input()

	for _ in range(int(N)):
		input = raw_input().split()

		if input[0] == "push":
			stack.push(input[1])

		if input[0] == "top":
			print stack.top()

		if input[0] == "size":
			print stack.size()

		if input[0] == "empty":
			print stack.empty()
			
		if input[0] == "pop":
			print stack.pop()