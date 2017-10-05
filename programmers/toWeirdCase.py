# https://programmers.co.kr/learn/challenge_codes/115
# coding:utf-8

def toWeirdCase(s):
    # 함수를 완성하세요
    words = s.split()

    space = []
    newWords = []

    for i in range(len(s)):
    	if s[i].isspace():
    		space.append(i)

    for word in words:
    	newWord = ''
    	for i in range(len(word)):
    		if i % 2 == 0 :
    			newWord += word[i].upper()

    		else:
    			newWord += word[i].lower()

    	newWords.append(newWord)

    newWords = list(''.join(newWords))
    
    for sp in space:
    	newWords.insert(sp, ' ')

    return ''.join(newWords)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));