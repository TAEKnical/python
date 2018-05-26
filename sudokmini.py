import random
def create_board():
	made = []
	for i in range(4):
		seed=[1,2,3,4]
		random.shuffle(seed)
		made.append(seed)
	return made

def shuffle_ribbons(board):
	top = board[:2]
	bottom=board[2:]
	random.shuffle(top)
	random.shuffle(bottom)
	return top + bottom

def transpose(board):
	transposed = [[],[],[],[]]
	for i in range(len(board)):
		for j in range(len(board)):
			transposed[i].append(board[j][i])
	return transposed

def creat_solution_board():
	board = create_board()
	board = shuffle_ribbons(board)
	board = transpose(board)
	board = shuffle_ribbons(board)
	board = transpose(board)
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
		i = random.randint(0,3)
		j = random.randint(0,3)
		if board[i][j] == 0:
			continue
		board[i][j] = 0
		holeset.add((i,j))
		no_of_holes-=1
	return board, holeset

def show_board(board):
	print()
	print('S','|','1','2','3','4')
	print('-','+','-','-','-','-')
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
	while not (number.isdigit() and 1<=int(number) and int(number)<=4): # 괄호 안에 조건식을 채운다.
		number = input(message)
	return int(number)

def sudokmini():
	solution = creat_solution_board()
	no_of_holes = get_level()
	puzzle = copy_board(solution)
	(puzzle,holeset)=make_holes(puzzle,no_of_holes)
	show_board(puzzle)
	while no_of_holes>0 :
		i = get_integer("가로줄번호(1~4): ",1,4)-1
		j = get_integer("세로줄번호(1~4): ",1,4)-1
		if (i,j) not in holeset:
			print("빈칸이 아닙니다.")
			continue
		n = get_integer("숫자(1~4): ", 1,4)
		sol = solution[i][j]
		if n == sol:
			puzzle[i][j] = sol
			show_board(puzzle)
			holeset.remove((i,j))
			no_of_holes-=1
		else:
			print(n, "가 아닙니다. 다시 해보세요.")

	print("잘 하셨습니다. 또 돌려주세요.")

sudokmini()