class Queue:
	queue = []

	def push(self, var):
		self.queue.append(var)

	def pop(self):
		if len(self.queue) == 0:
			return -1
		else:
			return self.queue.pop(0)

	def size(self):
		return len(self.queue)

	def empty(self):
		if self.size() == 0:
			return 1
		else:
			return 0

	def front(self):
		if self.empty == 0:
			return -1
		else:
			return self.queue[0]

	def back(self):
		if self.empty == 0:
			return -1
		else:
			return self.queue[-1]


que = Queue()

N = raw_input()

for case in range(int(N)):

	input = raw_input().split()

	if input[0] == "push":
		que.push(input[1])

	elif input[0] == "pop":
		print que.pop()

	elif input[0] == "size":
		print que.size()

	elif input[0] == "empty":
		print que.empty()

	elif input[0] == "front":
		print que.front()

	elif input[0] == "back":
		print que.back()

	print que.queue