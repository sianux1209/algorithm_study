# coding:utf-8

def water_melon(n):
    ward = "수박"
    ward *= int(n/2)

    if n % 2 != 0:
    	ward += "수"
    	
    return ward


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
