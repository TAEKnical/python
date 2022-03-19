# def radixsort(s1,s1_size):
# 	result=[]
# 	s2=[[],[],[],[],[],[],[],[],[],[]]
# 	j=-1
# 	while(j>-len(s1[0])-1):
	
# 		for i in range(len(s1)):
# 			s2[int(s1[i][j])].append(s1[i])

# 		for i in range(len(s2)):
# 			if(s2[i] !=[]):
# 				s1.append(s2[i])
# 			result+=s2[i]

# 		s1=result
# 		s2=[[],[],[],[],[],[],[],[],[],[]]
# 		j=j-1
					
# 	return s1

#기수정렬
def radixsort(s1,s1_size):
	if(s1==[]):
		return []
	j=-1
	while(j>-(len(s1[0]))-1):
		s2 = [[],[],[],[],[],[],[],[],[],[],[]]
		tmp = [] 
		for i in range(len(s1)):
			s2[int(s1[i][j])].append(str(s1[i]))
		for i in range(len(s2)):
			tmp +=s2[i]
		s1 = tmp
		j-=1
	return s1
s1=["0508","0515","1225","0915","1111","0101","0318","0301","0815"]
s1_size = 4
print(radixsort(s1,s1_size))