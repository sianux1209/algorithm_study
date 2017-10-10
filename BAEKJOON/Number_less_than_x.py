# https://www.acmicpc.net/problem/10871

N, X = map(int, raw_input().split())
li = map(int, raw_input().split())

li = [n for n in li if n < X]

print ' '.join(map(str, li))