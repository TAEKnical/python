def bin_search_closest(s,key):
	distance=[]	
	tmp=s[:]
		
	while(s !=[]):
		mid=len(s)//2
		if key not in s:
			for i in range(len(s)):
				distance.append(abs(key-s[i]))
			return distance.index(min(distance))
		else:
			if key ==s[mid]:
				return tmp.index(key)
			elif key<=s[mid]:
				s=s[:mid]
			else:
				s=s[mid+1:]
	return None

s=[1,4,6,7,10]
print(bin_search_closest(s,0))
