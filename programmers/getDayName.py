# coding:utf-8
import datetime

def getDayName(a,b):
	return ['MON','TUE','WED','THU','FRI','SAT','SUN'][datetime.datetime(2016, a, b).weekday()]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))