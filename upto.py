# def issymmetric(mat):
#     count = 0
#     size = len(mat)
#     i=1
#     for i in range(size):
#         for j in range(i):
#             count += 1 # count = count + 1 의 다른 표현
#             if mat[i][j] != mat[j][i]:
#                 return False
#     print(count,"번 비교")
#     return True

# m0 = [[ 1, 9,  5, 11],
#       [ 9, 4,  7,  3],
#       [ 5, 7, -7,  8],
#       [11, 3,  8,  6]]
# print(issymmetric(m0))




# #단위행렬 확인
# def isidentity(sqmat):
#     size = len(sqmat)
#     for i in range(size):
#         for j in range(size):
#             if i==j and sqmat[i][j]!=1 :
#                 return False
#             elif i!=j and sqmat[i][j]!=0 :
#                 return False
#     return True
# #스도쿠 확인
# def issudoku(mat):
# 	tmp = []
# 	size = len(mat)*len(mat)
# 	for i in range(len(mat)):
# 		for j in range(len(mat)):
# 			tmp.append(mat[i][j])
# 	tmp.sort()
# 	for i in range(size-1):
# 		if tmp[i] == 0:
# 			return False
# 		if not tmp[i] < tmp[i+1]:
# 			return False
# 	return True 


# m0 = [[ 1, 2,  3, 4],
# [ 5, 6,  7,  8],
# [ 9, 10, 11,  12],
# [13, 14,  15,  16]]
# print(issudoku(m0))

# #전치행렬
# def transpose(mat):
# 	no_of_columns = len(mat[0]) #바뀌기 전 열의 개수 = 바꾼 후 행의 개수
# 	no_of_hang = len(mat)
# 	transposed = []

# 	for i in range(no_of_columns):
# 		transposed.append([])
# 	for i in range(no_of_columns):
# 		for j in range(no_of_hang):
# 			transposed[j].append(mat[i][j]) 

# 	return transposed


# m0 = [[ 1, 2,  3, 4],
# [ 5, 6,  7,  8],
# [ 9, 10, 11,  12],
# [13, 14,  15,  16]]
# print(transpose(m0))









