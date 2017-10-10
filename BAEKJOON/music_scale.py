# https://www.acmicpc.net/problem/2920

scale = ["1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1"]

input = raw_input()

if input == scale[0]:
	print "ascending"

elif input == scale[1]:
	print "descending"
	
else:
	print "mixed"