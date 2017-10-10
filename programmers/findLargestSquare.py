# https://programmers.co.kr/learn/challenge_codes/189
# coding:utf-8



def findLargestSquare(board):
    answer = 0

    length = len(board[0])
    x, y = 0

    # length의 정사각형 생성이 가능한 위치면 생성 시도
    for i in range(length):
		for j in range(length):
			if board[i][j] == 'X':
				return False





    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))