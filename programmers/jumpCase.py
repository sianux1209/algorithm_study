# coding:utf-8

def jumpCase(num):
	if num == 1:
		return 1

	elif num == 2:
		return 2

	answer = jumpCase(num-1) + jumpCase(num-2)    
	return answer

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))
