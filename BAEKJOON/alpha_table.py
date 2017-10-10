input = raw_input()

li = []
table = "abcdefghijklmnopqrstuvwxyz"

for alpha in table:
	li.append(input.find(alpha))

print ' '.join(map(str, li))