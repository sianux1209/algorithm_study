# coding:utf-8

def caesar(s, n):

	encrypt = ''
	n = n % 26

	for i in range(len(s)):
		
		if s[i].isupper():
			temp = ord(s[i]) + n
			if temp > ord('Z'):
				temp -=26

			encrypt += chr(temp)

		elif s[i].islower():
			temp = ord(s[i]) + n
			if temp > ord('z'):
				temp -=26

			encrypt += chr(temp)

		else:
			encrypt += s[i]

	return encrypt
	# 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))