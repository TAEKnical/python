import random
def fresh_deck():
	suits = {"Spade", "Heart", "Diamond", "Club"}
	ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
	deck = []
	for suit in suits:
		for rank in ranks:
			tmp = {"suit":suit, "rank":rank}
			deck.append(tmp)
	random.shuffle(deck)
	return deck

def hit(deck):
	if deck==[]:
		deck = fresh_deck()
	card = deck[0]
	deck.remove(deck[0])
	return (card,deck)# (맨 앞의 카드 한장 , 남은 deck)

def count_score(cards):
	score = 0
	number_of_ace = 0
	for card in cards:
		tmp=card["rank"]
		if tmp=="A":
			number_of_ace+=1
			tmp=11
		if tmp in ["J","Q","K"]:
			tmp=10
		score+=int(tmp)
		while(score>21 and number_of_ace>0):
			score-=10
			number_of_ace-=1
	return score

def show_cards(cards,message):
	print(message)
	for card in cards:
		print("  "+card["suit"],card["rank"])
def show_dealer_cards(cards,message):
	print(message)
	number=1
	for card in cards:
		if(number==1):
			print("  **** **")
		else:
			print("  "+card["suit"],card["rank"])		
		number+=1
def more(message):
	answer = input(message)
	while answer not in ['y','n']:#(반복 조건):
		answer = input(message)
	return answer=='y'
def card_open(client,dealer):
	if count_score(client)==21 : #손님 블랙잭
		show_cards(dealer,"My cards are:")
		print("Blackjack! You won.")
		return "CBlackjack"
	if count_score(client)>21 :
		show_cards(dealer,"My cards are:")
		print("You bust! I won.")
		return "DWin"
	if count_score(dealer)>21: #딜러 버스트
		show_cards(dealer,"My cards are:")
		print("I bust! You won.")
		return "CWin"
	if count_score(client) == count_score(dealer): #무승부
		show_cards(dealer,"My cards are:")
		print("We draw.")
		return "Draw"
	if count_score(client)>count_score(dealer) and count_score(client) <21 and count_score(dealer)<21:
		show_cards(dealer,"My cards are:")
		print("You won.") #손님승
		return "CWin"
	show_cards(dealer,"My cards are:")
	print("I won.") #딜러 승
	return "DWin"

def load_members():
	file=open("members.txt", "r")
	members = {}
	for line in file:
		name, passwd, tries, wins, chips = line.strip('\n').split(',')
		members[name] = (passwd,int(tries), float(wins), int(chips))
	file.close()
	return members

def store_members(members):
	file = open("members.txt","w")
	names = members.keys()
	for name in names:
		passwd, tries, wins, chips = members[name]
		line = name + ',' + passwd + ',' + \
			str(tries) + ',' + str(wins) + "," + str(chips) + '\n'              
		file.write(line)
	file.close()

def login(members):
	username = input("Enter your name: (4 letters max) ")
	while len(username) > 4:
		username = input("Enter your name: (4 letters max) ")
	trypasswd = input("Enter your password: ")
	
	if username in members:
		passwd = members[username][0]
		tries = members[username][1]
		wins = members[username][2]
		chips = members[username][3]

		if members[username][1]>0: #나누기 오류방지
			percentage = float(wins)/float(tries)
		else:
			percentage = 0


		if passwd == trypasswd:
			print("You played",tries,"games and won",int(wins),"of them.")# username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
			print("Your all-time winning percentage is","{0:.1f}".format(percentage*100),"%") # 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
			print()
			if chips >= 0:# 칩 보유개수를 보여줌
				print("You have",chips,"chips.")
			else:
				print("You owe",chips,"chips.")
			return username, tries, wins, chips, members
		else:
			return login(members)
	else:
		members[username] = (trypasswd, 0, 0, 0) #뭐야 이게
		return username, 0, 0, 0, members # username을 members 사전에 추가한다.

def show_top5(members):
	print("-----")
	i=0
	sorted_members=sorted(members.items(),key=lambda x: x[1][1],reverse=True)# 칩의 개수 역순으로 정렬
	print("All-time Top 5 based on the number of chips earned")
	for name in sorted_members[:5]:
		if(sorted_members[i][1][3]==0):
			continue
		print(str(i+1)+". "+str(sorted_members[i][0])+" : "+str(sorted_members[i][1][3]))
		# print(i+1,name[0],name[i][3])
		i+=1
	# sorted_members[:5]의 원소를 차례대로 참고하여 보여주되 0이하는 무시한다.
def BlackJack():
	client_chip = 0
	dealer_chip = 0

	print("Welcome to SMaSH Casino!")
	members = load_members()
	username, tries, wins, chips, members = login(members)
	round_tries=0
	round_wins=0

	remain = fresh_deck()
	while True:#라운드 반복실행
		round_tries+=1 #게임횟수 추가

		print("-----")
		(card1,remain)=hit(remain)
		(card3,remain)=hit(remain)
		(card2,remain)=hit(remain)
		(card4,remain)=hit(remain)
		client=[card1,card2]
		dealer=[card3,card4]

		show_dealer_cards(dealer,"dealer`s cards are")
		show_cards(client,"clinet`s cards are") 
		while count_score(client)<21: #손님의 카드합이 21보다 작으면 받을지 말지 선택한다
			hitox=more("Hit? (y/n)")
			if hitox == True:
				(card,remain)=hit(remain)
				print(" ",card["suit"],card["rank"])
				client.append(card)
			else:
				break
		while count_score(dealer)<16: #딜러의 카드합이 16보다 작으면 무조건 받는다
			(card,remain)=hit(remain)
			dealer.append(card)

		result=card_open(client,dealer)
		if result == "CBlackjack":
			client_chip+=2
			round_wins+=1 #승수 추가
		elif result == "CWin":
			client_chip+=1
			round_wins+=1
		elif result == "DWin":
			client_chip-=1
		elif result == "Draw":
			round_wins+=0.5
		print("Chips =",client_chip)
		if more("Play more?(y/n)")==False:
			break
	percentage = (float(round_wins)/float(round_tries))*100
	print("Bye!")
	print("You played",round_tries,"and won",round_wins,"of them.")
	print("Your winning percentage today is","{0:.1f}".format(percentage),"%")
	wins+=round_wins
	tries+=round_tries
	chips +=client_chip #게임 종료시 칩 개수
	members[username] = (members[username][0],int(tries), float(wins), int(chips))
	store_members(members)
	show_top5(members)
BlackJack()