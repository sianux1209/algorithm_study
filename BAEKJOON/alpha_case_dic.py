# https://www.acmicpc.net/problem/1157

input = ""
input = input.lower()

dic = {}

for alpha in range(ord('a'), ord('z')):
	dic[chr(alpha)] = input.count(chr(alpha))

maxCount = max(dic.values())

maxWord = [k for k,v in dic.items() if v == maxCount]

print maxCount

print dic

if maxCount == 0

if len(maxWord) == 1 :
	print maxWord[0].upper()
else:
	print "?"
