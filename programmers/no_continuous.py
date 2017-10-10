# https://programmers.co.kr/learn/challenge_codes/86
# coding:utf-8

def no_continuous(s):
	return [s[i] for i in range(len(s)) if s[i] != s[i-1] or i==0]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))