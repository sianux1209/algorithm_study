# coding:utf-8

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum(map(int,str(n))) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))