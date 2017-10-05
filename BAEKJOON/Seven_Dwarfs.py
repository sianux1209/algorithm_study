# https://translate.google.com/?source=gtx#ko/en/%EC%9D%BC%EA%B3%B1%EB%82%9C%EC%9F%81%EC%9D%B4

import random

li = []
result = []

for _ in range(9):
	li.append(int(raw_input()))


while True:

	dwarfs = random.sample(li, 7)
	sum_result = sum(dwarfs)
	
	if sum_result == 100:
		break	

dwarfs.sort()
for dwarf in dwarfs:
	print dwarf