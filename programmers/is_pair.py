# https://programmers.co.kr/learn/challenge_codes/88
# coding:utf-8

def is_pair(s):
    
    pairCheck = 0

    for char in s:

    	if char == "(":
    		pairCheck += 1
    	elif char == ")":
    		pairCheck -=1

    	if pairCheck < 0 :
    		return False

    if pairCheck != 0:
    	return False

    return True


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))