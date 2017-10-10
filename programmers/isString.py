# https://programmers.co.kr/learn/challenge_codes/100
# coding:utf-8

def alpha_string46(s):
	if len(s) == 4 or len(s) == 6:
		return s.isdigit()

	return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )