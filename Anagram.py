def find_anagrams(d4s):
	if d4s == []:
		return []
	result = []
	tmp =[]
	for s1 in d4s:
		for s2 in d4s:
			string1=[]
			string2=[]
			if s1==s2:
				continue
			for i in range(len(s1)):
				string1.append(s1[i])
				string2.append(s2[i])
			string1.sort()
			string2.sort()
			if string1 == string2:
				if s1 not in tmp:
					tmp.append(s1)
				if s2 not in tmp:
					tmp.append(s2)
		tmp.sort()
		if (tmp != []) and (tmp not in result):
			result.append(tmp)
		tmp = []
	return result
print("result : ",find_anagrams(["0952", "5239", "1270", "8581", "7458",
 "3414", "7906", "2356", "4360", "3491",
 "6232", "5927", "2735", "2509", "5849",
 "8457", "9340", "1858", "8602", "5784"]))