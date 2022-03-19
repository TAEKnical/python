#숙제 계싼횟수찾기
def minsteps(n):
	memo = [0] * (n + 1)
	memo2 = [0] * (n+1)
	nn=n
	nnn=n
	count = 0
	count2=0
	j=1
	i=1
	for i in range(n+1):
		while(nn!=1):
			if nn%3==0:
				nn=nn//3
			elif nn%2==0:
				nn=nn//2
			else:
				nn=nn-1
			count=count+1
		memo[i] = count
	for i in range(n+1):
		while(nnn!=1):
			if nnn%3 !=0 and (nnn-1)%3==0:
				nnn=nnn-1
			elif nnn%3==0:
				nnn=nnn//3
			elif nnn%2==0:
				nnn=nnn//2
			else:
				nnn=nnn-1
			count2=count2+1
		memo2[i] = count2	
	return min(memo[n],memo2[n])
print(minsteps(514))