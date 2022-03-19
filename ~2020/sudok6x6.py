import random
def creat_board():
	seed = [1,2,3,4,5,6]
	random.shuffle(seed)
	n1 = seed[0]
	n2 = seed[1]	
	n3 = seed[2]
	n4 = seed[3]
	n5 = seed[4]
	n6 = seed[5]
	made=[[n1,n2,n3,n4,n5,n6],
		[n4,n5,n6,n1,n2,n3],
		[n3,n1,n2,n6,n4,n5],
		[n6,n4,n5,n3,n1,n2],
		[n2,n3,n1,n5,n6,n4],
		[n5,n6,n4,n2,n3,n1]]
	return made

def shuffle_ribbons(board):
	top = board[:2]
	mid = board[2:4]
	bottom = board[4:]
	random.shuffle(top)
	random.shuffle(mid)
	random.shuffle(bottom)
	return top + mid + bottom

def transpose(board):
	transposed = [[],[],[],[],[],[]]
	for i in range(len(board)):
		for j in range(len(board)):
			transposed[i].append(board[j][i])
	return transposed

def creat_solution_board():
	board = creat_board()
	board = shuffle_ribbons(board)
	board = transpose(board)
	board = shuffle_ribbons(board)
	board = transpose(board)
	for i in range(6):
		print(board[i])

	return board

def get_level():
	level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
	while level not in {"상","중","하"}:
		level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
	if level == '하':
		return 6
	elif level == '중':
		return 8
	elif level == '상':
		return 10

def copy_board(board):
	board_clone = []
	for row in board:
		row_clone = row[:]
		board_clone.append(row_clone)
	return board_clone 

def make_holes(board, no_of_holes):
	holeset = set()
	while no_of_holes>0:
		i = random.randint(0,5)
		j = random.randint(0,5)
		if board[i][j] == 0:
			continue
		board[i][j] = 0
		holeset.add((i,j))
		no_of_holes-=1
	return board, holeset

def show_board(board):
	print()
	print('S','|','1','2','3','4','5','6')
	print('-','+','-','-','-','-','-','-')
	r=0
	for row in board:
		print(r+1,"|",end="")
		for i in range(len(board)):
			if row[i] == 0:
				print("",".",end="")
				continue
			print("",row[i],end="")
		print()
		r+=1

def get_integer(message,i,j):
	number = input(message)
	while not (number.isdigit() and 1<=int(number) and int(number)<=6): # 괄호 안에 조건식을 채운다.
		number = input(message)
	return int(number)

def sudokmini():
	solution = creat_solution_board()
	no_of_holes = get_level()
	puzzle = copy_board(solution)
	(puzzle,holeset)=make_holes(puzzle,no_of_holes)
	show_board(puzzle)
	while no_of_holes>0 :
		i = get_integer("가로줄번호(1~6): ",1,6)-1
		j = get_integer("세로줄번호(1~6): ",1,6)-1
		if (i,j) not in holeset:
			print("빈칸이 아닙니다.")
			continue
		n = get_integer("숫자(1~4): ", 1,6)
		sol = solution[i][j]
		if n == sol:
			puzzle[i][j] = sol
			show_board(puzzle)
			holeset.remove((i,j))
			no_of_holes-=1
		else:
			print(n, "가 아닙니다. 다시 해보세요.")

	print("잘 하셨습니다. 또 돌려주세요.")
sudokmini() #실행

