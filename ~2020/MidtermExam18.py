#  #1
# def complement9(n): # 자연수라고 가정
# 	s = str(n)
# 	ans = ""
# 	for c in s:
# 		distance=abs(9-int(c))
# 		ans=ans+str(distance)
# 	return int(ans)
# print(complement9(0))
# print(complement9(9))
# print(complement9(4))
# print(complement9(18))
# print(complement9(40))
# print(complement9(307))
# print(complement9(9999))
# print(complement9(9142))
# print(complement9(9965))


# #2
# def search(key,ns):
#     index = 0
#     result=[]
#     for n in ns:
#         if key == n:
#             result.append(index)
#             index+=1
#         else:
#             index += 1
#     return result
# print(search(3,[])) # []
# print(search(3,[4,6,3,3,3])) # [2,3,4]
# print(search(3,[3,3,3,3,3])) # [0,1,2,3,4]
# print(search(3,[4,2,7,6,5])) # []

# #3
# def count_upto(n):
# 	def loop(n,ns):
# 		if n < 0:
# 			return [] # 이 부분을 채우자
# 		else:
# 			return loop(n-1,ns)+[n] # 이 부분을 채우자
# 	return loop(n,[])

# print(count_upto(0)) # [0]
# print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
# print(count_upto(-3)) # []

# #4
# def count_upto(n):
# 	ns = []
# 	if n<0:
# 		return []
# 	while n>=0: # 이 부분을 채우자
# 		ns=[n]+ns # 이 부분을 채우자
# 		n-=1
# 	return ns
# print(count_upto(0)) # [0]
# print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
# print(count_upto(-3)) # []

#5 다시
# def zippo(xs,ys):
# 	def loop(xs,ys,zs):
# 		if xs == [] or ys == []:
# 			return xs+ys # 이 부분을 채우자
# 		else:
# 			zs.append(xs[0]+ys[0])
# 			zs=zs+loop(xs[1:],ys[1:],[])
# 			return zs
# 	return loop(xs,ys,[])
# print(zippo([],[])) # []
# print(zippo([2,7,4],[7,2,5])) # [9,9,9]
# print(zippo([2,7,4],[7,2,5,9,9])) # [9,9,9,9,9]
# print(zippo([2,7,4,9,9],[7,2,5])) # [9,9,9,9,9]

# #6
# def zippo(xs,ys):
# 	zs = []
# 	while xs!=[] and ys!=[]: # 이 부분을 채우자
# 		zs.append(xs[0]+ys[0])
# 		xs=xs[1:]
# 		ys=ys[1:]
# 	return zs + xs + ys
# print(zippo([],[])) # []
# print(zippo([2,7,4],[7,2,5])) # [9,9,9]
# print(zippo([2,7,4],[7,2,5,9,9])) # [9,9,9,9,9]
# print(zippo([2,7,4,9,9],[7,2,5])) # [9,9,9,9,9]


# #7
# def blast(ns):
# 	bs = []
# 	for i in ns:
# 		for j in range(i):
# 			bs.append(i)
# 	return bs
# print(blast([]))
# print(blast([1,2,4]))
# print(blast([3,5]))
# print(blast([2,-3,3]))

# #8
# def union(xs,ys):
# 	tmp=[]
# 	for x in xs:
# 		if x not in tmp:
# 			tmp.append(x)
# 	for y in ys:
# 		if y not in tmp:
# 			tmp.append(y)
# 	return tmp

# print(union([1,2,3,4,5],[1,2,3,6,7,8,9,10]))
# print(union([3,2,4],[1,2,3]))

# #9
# def diff(xs,ys):
# 	xs1=[]
# 	ys1=[]
# 	for i in range(len(xs)):
# 		if xs[i] not in xs1:
# 			xs1.append(xs[i])
# 	for j in range(len(ys)):
# 		if ys[j] not in ys1:
# 			ys1.append(ys[j])
# 	tmp=[]
# 	for k in range(len(xs1)):
# 		if xs1[k] not in ys1:
# 			tmp.append(xs1[k])
# 	return tmp

# print(diff([1,2,2,3,3,3,4,4,5,5,5],[1,2,3,6,7,8,9,10]))
# print(diff([3,2,4],[1,2,3]))

# # #10
# def intersect(xs,ys):
# 	xs1=[]
# 	ys1=[]
# 	tmp=[]
# 	for i in range(len(xs)):
# 		if xs[i] not in xs1:
# 			xs1.append(xs[i])
# 	for j in range(len(ys)):
# 		if ys[j] not in ys1:
# 			ys1.append(ys[j])
# 	for k in range(len(xs1)):
# 		if xs1[k] in ys:
# 			tmp.append(xs1[k])
# 	return tmp
# print(intersect([1,2,2,3,3,3,4,4,5,5,5],[1,2,3,3,6,7,8,9,10]))
# print(intersect([3,2,4],[1,2,3]))

#11 다시
# def equiv_class(ns):
# 	ns.sort()
# 	index=0
# 	if ns == []:
# 		return []
# 	else:
# 		top = ns[0]
# 		nss = [[top]]
# 		for n in ns[1:]:

# 	return nss

# print(equiv_class([]))
# print(equiv_class([3]))
# print(equiv_class([4,3,2,4,4]))
# print(equiv_class([2,4,4,2,2,3]))

# #12 다시
def perm(xs):
      subs = [[]]
      k=len(xs)
      for i in range(len(xs)-k+1):
            subs.append(xs[i:i+k])
            k-=1
      return subs

print(perm([]))
print(perm([1]))
print(perm([1,2]))
print(perm([1,2,3]))
print(perm([1,2,3,4]))