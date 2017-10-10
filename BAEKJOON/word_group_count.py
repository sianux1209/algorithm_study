#https://www.acmicpc.net/problem/1152

input = raw_input().split()
input = [int(input[0][::-1]), int(input[1][::-1])]
print max(input)