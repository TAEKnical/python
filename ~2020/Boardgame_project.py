global rank
import random

def choose_character():
	character = input("캐릭터를 선택해 주세요. 정마담/아귀/고니 ")
	global User
	global AI1
	global AI2
	while not (character == '정마담' or character == '아귀' or character == '고니'):
		character = input("캐릭터를 선택해 주세요. 정마담/아귀/고니")
		if character == '정마담':
			User = {'이름' : '정마담' , 'Start_money' : 500000, 'Skill_list' : 1, 'Skill_use' : 5}
			AI1 = {'이름' : '아귀' , 'Start_money' : 750000, 'Skill_list' : 1, 'Skill_use' : 3}
			AI2 = {'이름' : '고니' , 'Start_money' : 300000, 'Skill_list' : 1, 'Skill_use' : 7}
		elif character == '아귀':
			User = {'이름' : '아귀' , 'Start_money' : 750000, 'Skill_list' : 1, 'Skill_use' : 3}
			AI1 = {'이름' : '고니' , 'Start_money' : 300000, 'Skill_list' : 1, 'Skill_use' : 7}
			AI2 = {'이름' : '정마담' , 'Start_money' : 500000, 'Skill_list' : 1, 'Skill_use' : 5}
		elif character == '고니':
			User = {'이름' : '고니' , 'Start_money' : 300000, 'Skill_list' : 1, 'Skill_use' : 7}
			AI1 = {'이름' : '정마담' , 'Start_money' : 500000, 'Skill_list' : 1, 'Skill_use' : 5}
			AI2 = {'이름' : '아귀' , 'Start_money' : 750000, 'Skill_list' : 1, 'Skill_use' : 3}



def fresh_deck():
	deck = []
	for i in range(10):
		deck.append(i+1)
		deck.append(-(i+1))
	random.shuffle(deck)
	return deck


def hit(deck):
	if deck == []:
		fresh_deck()
	return  (deck[0],deck[1:])


def show_cards(cards):
	for card in cards:
		print(card) # 패 표현방법 바꿔야됨


def more(message):
	answer = input(message)
	while not (answer == 'y' or answer == 'n'):
		answer = input(message)
	return answer == 'y'


# # #족보
def mangtong(cards):
	if 3 in cards and (7 in cards or -7 in cards):
		print('망통이다')
		# rank += 0
	elif -3 in cards and -7 in cards:
		print('망통이다')
		rank += 0
		
	elif 2 in cards and (8 in cards or -8 in cards):
		print('망통이다')
		rank += 0
	elif -2 in cards and (8 in cards or -8 in cards):
			print('망통이다')
			rank += 0
	# return rank

# def gap5():

def sae6(cards):
	if 4 in cards and (6 in cards or -6 in cards):
			print('세륙이다')
			rank += 2
	elif -4 in cards and (6 in cards -6 in cards):
			print('세륙이다')
			rank += 2
	return rank

def jangsa(cards):
	if 4 in cards and (10 in cards or -10 in cards):
			print('장사다')
			rank += 3
	elif -4 in cards and (10 in cards or -10 in cards):
			print('장사다')
			rank += 3
	return rank
	# if (4 and 10 in cards) or (-4 and 10 in cards) or (4 and -10 in cards) or (-4 and -10 in cards):
	# 	print('장사다')
	# 	rank += 2


	
# def gap5():  #더해서 9 or 19() #(18	
# 	if (cards[0].get('number') + cards[1].get('number')) == 9 or  :
		
# 	return rank += 1

def jangbbing(cards):
	if 1 in cards and (10 in cards or -10 in cards):
			print('장삥이다')
			rank += 4
	elif -1 in cards and (10 in cards or -10 in cards):
			print('장삥이다')
			rank += 4
	return rank


def gubbing(cards):
	if 1 in cards and (9 in cards or -9 in cards):
			print('구삥이다')
			rank += 5
	elif -1 in cards and (9 in cards or -9 in cards):
			print('구삥이다')
			rank += 5
	return rank

def docksa(cards):
	if 1 in cards and (4 in cards or -4 in cards):
			print('독사다')
			rank += 6
	elif -1 in cards and (4 in cards or -4 in cards):
			print('독사다')
			rank += 6
	return rank

def alri(cards):
	if 1 in cards and (2 in cards -2 in cards):
			print('알리다')
			rank += 7
	elif -1 in cards and (2 in cards or -2 in cards):
			print('알리다')
			rank += 7
	return rank

def ddang(cards):
	if cards[0] == cards[1]:
		print(cards[0],'땡이다')
		rank += 8
	return rank

def guangddang():
	if 1 in cards:
		if 3 in cards:
			print('13광땡이다')
			rank += 9
		elif 8 in cards:
			print('18광떙이다')
			rank += 9
	elif 3 in cards:
		if 8 in cards:
			print('38광땡이다')
			rank += 9


def sutda():	
	computer_money = 1000# 초기자금
	player_money = 1000
	
	def game(computer_money,player_money):

		while computer_money > 0 and player_money > 0:
			print("섯다시작")
			deck = fresh_deck()
			computer = []
			player = []
			computer_rank = 0
			player_rank = 0
			betting_money = 0
			card, deck = hit(deck)
			player.append(card)
			card, deck = hit(deck)
			computer.append(card)
			show_cards(player)
			bet = input('얼마 거시겠습니까?')
			betting_money += int(bet)
			card, deck = hit(deck)
			player.append(card)
			card, deck = hit(deck)
			computer.append(card)
			print("내 패는:")
			show_cards(player)
			bet = input('얼마 거시겠습니까?')
			betting_money += int(bet)
			more_betting = more('더 배팅하시겠습니까?')
			if more_betting:
				bet = input('얼마 거시겠습니까?')
				betting_money += int(bet)
			#족보일경우 rank 값으로 승패 결정
			# mangtong(player)
			# sae6()
			# jangbbing()
			# jangsa()
			# ddang()
			# guangddang()
			# gubbing()
			# alri()
			#족보가 아닌경우 패의 숫자로 승패 결정
			



			if player_rank > computer_rank:
				print("player win")
				computer_money -= betting_money
				player_money += betting_money
				# winmoney = (money + int(bet))
				print(player_money) # 질경우 돈
				print(computer_money)

			elif player_rank < computer_rank:
				print("computer win")
				computer_money += betting_money
				player_money -= betting_money
				# losemoney = (money - int(bet))
				print(player_money) # 질경우 돈
				print(computer_money)
			elif player_rank == computer_rank: # (끗일떄는 일의자리수에서 대소비교), 떙이랑 광은 상관 x 
				player_score = abs(player[0]) + abs(player[1])
				computer_score = abs(computer[0]) + abs(computer[1])
				if player_score > computer_score:
					print("player win")
					computer_money -= betting_money
					player_money += betting_money
					# winmoney = (money + int(bet))
					print(player_money) # 질경우 돈
					print(computer_money)
					
				elif player_score < computer_score:
					print("computer win")
					computer_money += betting_money
					player_money -= betting_money
					# losemoney = (money - int(bet))
					print(player_money) # 질경우 돈
					print(computer_money)
				else:
					print('비김')
					game(computer_money,player_money) #판돈그대로 묻고 다음게임 진행
			
			
		return computer_money,player_money
	game(computer_money,player_money)
sutda()