T = int(raw_input())

li = []

for n in range(T):
	li.append(int(raw_input()))


li.sort()
print "\n".join(map(str,li))