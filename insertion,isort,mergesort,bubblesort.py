# #isort while버전

# def insert(x,ss):
# 	if ss != []:
# 		if x <= ss[0]:
# 			return [x]+ss[:]
# 		else:
# 			tmp = ss[0]
# 			ss.remove(ss[0])
# 			return [tmp]+insert(x,ss)
# 	else:
# 		return ss[:]+[x]

# def isort1(s):
# 	def loop(s,ss):
# 		while(s != []):
# 			temp=s[0]
# 			s.remove(s[0])
# 			return loop(s[:],insert(temp,ss))
# 		return ss
# 	return loop(s,[])

# s=[3,5,4,2]
# print(isort1(s))


# def insert(x,ss):
# 	if ss != []:
# 		if x <= ss[0]:
# 			return [x]+ss[:]
# 		else:
# 			tmp = ss[0]
# 			ss.remove(ss[0])
# 			return [tmp]+insert(x,ss)
# 	else:
# 		return ss[:]+[x]

# def isort1(s):
# 	def loop(s,ss):
# 		# while(s != []):
# 		for i in range()
# 			temp=s[0]
# 			s.remove(s[0])
# 			return loop(s[:],insert(temp,ss))
# 		return ss
# 	return loop(s,[])

# s=[3,5,4,2]
# print(isort1(s))

# #ISORT for 루프버전
# def insert2(x,ss):
#    left = []
#    while ss != []:
#       if x <= ss[0]:
#          return left + [x] + ss
#       else:
#          ss, left = ss[1:], left + [ss[0]]
#    return left + [x]
# def isort(s):
#    ss = []
#    for x in s:
#       s,ss = s[1:],insert2(s[0],ss)
#    return ss

# #합병정렬 재귀
# def merge0(left,right):
# 	if not (left==[] or right == []):
# 		if(left[0]<=right[0]):
# 			return [left[0]]+merge0(left[1:],right)
# 		else:
# 			return [right[0]]+merge0(left,right[1:])
# 	else:
# 		return left+right


# def msort0(s):
# 	if len(s) > 1:
# 		mid = len(s) // 2
# 		return merge0(msort0(s[:mid]),msort0(s[mid:]))
# 	else:
# 		return s

# s=[32,23,18,7,11,99,55]
# print(msort0(s))

# #합벙정렬 꼬리재귀
# def merge1(left,right):
#     def loop(left,right,ss):
#         if not (left == [] or right == []):
#             if left[0] <= right[0]:
#                 ss.append(left[0])
#                 left.remove(left[0])
#                 return loop(left,right,ss)
#             else:
#                 ss.append(right[0])
#                 right.remove(right[0])
#                 return loop(left,right,ss)
#         else:
#             return ss+left+right
#     return loop(left,right,[])
# def msort0(s):
#     if len(s) > 1:
#         mid = len(s) // 2
#         return merge1(msort0(s[:mid]),msort0(s[mid:]))
#     else:
#         return s
# s=[32,23,18,7,11,99,55]
# print(msort0(s))

# #합병정렬 While
# def merge(left,right):
# 	ss=[]
# 	while not (left ==[] or right == []):
# 		if left[0] <= right[0]:
# 			ss.append(left[0])
# 			left.remove(left[0])
# 		else:
# 			ss.append(right[0])
# 			right.remove(right[0])
# 	return ss+left+right
# def msort0(s):
#     if len(s) > 1:
#         mid = len(s) // 2
#         return merge(msort0(s[:mid]),msort0(s[mid:]))
#     else:
#         return s

# s=[32,23,18,7,11,99,55]
# print(msort0(s))

# ★#퀵정렬
# def partition(pivot,s):
#     left, right = [], []
#     for x in s:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
#     return left, right
# def qsort(s):
#     if len(s) > 1:
#         pivot = s[0]
#         (left, right) = partition(pivot,s[1:])
#         return qsort(left) + [pivot] + qsort(right)
#     else:
#         return s
# s=[3,7,8,5,2,1,9,5,4]
# print(qsort(s))

# #버블정렬 for버전
# def bsort(s):
#     for k in range(len(s-1)):
#         for i in range(len(s)-1):
#             if s[i] > s[i+1]:
#                 s[i], s[i+1] = s[i+1], s[i]
#     return s
# s=[3,7,8,5,2,1,9,5,4]
# print(bsort(s))

# #버블정렬 for버전//교수님
# def bsort(s):
#     for k in range(len(s)-1,0,-1):
#         for i in range(k):
#             if s[i] > s[i+1]:
#                 s[i], s[i+1] = s[i+1], s[i]
#     return s
# s=[3,7,8,5,2,1,9,5,4]
# print(bsort(s))