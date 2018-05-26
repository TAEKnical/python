# 실습1 펠린드롬
# def is_pal(s):
#     return (len(s)<= 1) or ( (s[0] == s[-1]) and (is_pal(s[1:-1]) ) )

# #실습 2
# def fillwith(sentence):
#     new_sentence = ''
#     for char in sentence:
#         # if char==new_sentence:
#         #     print("공백이래요")

#         if(char == ' '):
#             char = '_'
#         new_sentence += char
#     return new_sentence
# print(fillwith('따스한 봄 나들이 갑시다.'))

#실습3
# def add_range(start,stop,step):
#     sum = 0
#     i = start
#     for i in range(start,stop,step):
#         sum += i
#     return sum


#실습4
# def vowl_number(word):
#     new=''
#     count = 0
#     for char in word:
#         if char in ['a','e','i','o','u','A','E','I','O','U']:
#             count+=1
#             char=str(count)
#         new += char
#     return new

#실습5(1)
#while버전
# def greatest(s):
#     if len(s)==0:
#         return None
#     else:
#         top=s[0]
#         while s!=[]:
#             if s[0]>top:
#                 top=s[0]
#             s=s[1:]
#         return top
# print(greatest([5,2,3,6,4,3,7,5,8,2])) # 8
# print(greatest([5,2])) # 5
# print(greatest([5])) # 5
# print(greatest([])) # None
# #for버전
# def greatest(s):
#     if len(s)==0:
#         return None
#     else:
#         top=s[0]
#         for i in range(1,len(s)):
#             if s[i]>top:
#                 top = s[i]
#         return top
# print(greatest([5,2,3,6,4,3,7,5,8,2])) # 8
# print(greatest([5,2])) # 5
# print(greatest([5])) # 5
# print(greatest([])) # None
# #5-(2)
# def greatest(s):
#     if len(s)==0:
#         return None
#     else:
#         top=s[0]
#         for i in range(1,len(s)):
#             if s[i]>top:
#                 top = s[i]
#         return top
# def rankith(s,n):
#     for i in range(n-1):
#         s.remove(greatest(s))
    
#     return greatest(s)
# print(rankith([5,2,3,6,4,3,7,5,8,2],1)) # 8
# print(rankith([5,2,3,6,4,3,7,5,8,2],2)) # 7
# print(rankith([5,2,3,6,4,3,7,5,8,2],4)) # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],5)) # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],6)) # 4
# print(rankith([5,2],2)) # 2
# print(rankith([5],1)) # 5
# print(rankith([],1)) # None




# #실습6 가장 많이 반복된 수와 횟수 찾기
# def longest_repetition(s):
#     if s != []:
#         record = s[0]   # 지금까지 가장 큰 수
#         recordtimes = 1 # 그 수의 연속반복 횟수
#         on = s[0]       # 현재 검사하고 있는 수
#         ontimes = 1     # 그 수의 연속반복 횟수
#         for n in s[1:]:
#             if on==n:
#                 ontimes+=1
#                 if ontimes>recordtimes:
#                     record=on
#                     recordtimes=ontimes
#             else:
#                 on = n
#                 ontimes=1          
#         return (record,recordtimes)
#     else:
#         return (None,0)
# print(longest_repetition([5,5,4,4,4,4,4,2,2,2,2,7,8,4,4,3,3,3]))
# print(longest_repetition([2,2,2]))
# print(longest_repetition([]))
# #선국이형꺼
# def longest_repetition(s):
#     if s != []:
#         s.sort()
#         record = s[0]   # 지금까지 가장 큰 수
#         recordtimes = 1 # 그 수의 연속반복 횟수
#         on = s[0]       # 현재 검사하고 있는 수
#         ontimes = 1     # 그 수의 연속반복 횟수
#         for n in s[1:]:
#             if(on == n):
#                 ontimes += 1
#                 if(ontimes > recordtimes):
#                     recordtimes = ontimes
#                     record = on
#             else:
#                 on = n
#                 ontimes = 1
#         return (record,recordtimes)
#     else:
#         return (None,0)



#실습7 삼각수
# # 재귀함수
# def trinum(n):
#     if n >= 1:
#         return  n+trinum(n-1)# 여기에 알맞은 코드를 채워 넣자.
#     else:
#         return 0 # 여기에 알맞은 코드를 채워 넣자.
# # 테스트 케이스
# print(trinum(1)) # 1
# print(trinum(3)) # 6
# print(trinum(6)) # 21
# print(trinum(11)) # 66
# print(trinum(0)) # 0
# print(trinum(-3)) # 0
# 꼬리재귀함수
# def trinum(n):
#     def loop(n,r):
#         if n>=1:
#             r=n+loop(n-1,r)
#             return r
#         else:
#             return 0
#     return loop(n,0) # 여기에 알맞은 코드를 채워 넣자.
# # 테스트 케이스
# print(trinum(1))
# print(trinum(3)) #6
# print(trinum(6)) #21
# print(trinum(11)) #66
# print(trinum(0)) #0
# print(trinum(-3)) #0
# # while 루프 함수
# def trinum(n):
#     sum=0
#     while(n>=1):
#         sum+=n
#         n-=1
#     return sum
# # 테스트 케이스
# print(trinum(1)) # 1
# print(trinum(3)) # 6
# print(trinum(6)) # 21
# print(trinum(11)) # 66
# print(trinum(0)) # 0
# print(trinum(-3)) # 0
# # for 루프 함수
# def trinum(n):
#     i=1
#     sum=0
#     for i in range(n+1):
#         sum+=i
#     return sum
# # 테스트 케이스
# print(trinum(1)) # 1
# print(trinum(3)) # 6
# print(trinum(6)) # 21
# print(trinum(11)) # 66
# print(trinum(0)) # 0
# print(trinum(-3)) # 0



# #실습8 더하기로 제곱구하기 꼬리재귀
# # 꼬리 재귀
# def square(n):
#     def loop (n,sum):
#         if n>0:
#             sum = sum + (2*n-1)
#             return loop(n-1,sum)
#         else:
#             return sum
#     return loop(abs(n),0)
# print(square(0)) # => 0
# print(square(1)) # => 1
# print(square(-2)) # => 4
# print(square(3)) # => 9
# print(square(-4)) # => 16
# print(square(5)) # => 25
# # while 루프
# def square(n):
#     n=abs(n)
#     sum=0
#     while(n>0):
#         sum += 2*n-1
#         n-=1
#     return sum
# print(square(0)) # => 0
# print(square(1)) # => 1
# print(square(-2)) # => 4
# print(square(3)) # => 9
# print(square(-4)) # => 16
# print(square(5)) # => 25
# #for루프
# def square(n):
#     n=abs(n)
#     sum=0
#     for i in range(n,0,-1):
#         sum+=2*i-1
#     return sum
# print(square(0)) # => 0
# print(square(1)) # => 1
# print(square(-2)) # => 4
# print(square(3)) # => 9
# print(square(-4)) # => 16
# print(square(5)) # => 25



#실습9 주어진 문자 모두 지우기
#재귀버전
# def remove(x,xs):
#     if x not in xs:
#         return xs
#     else:
#         a=xs.partition(str(x))
#         xs=a[0]+a[2]
#         return remove(x,xs)
# # 테스트 케이스
# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))
# # 꼬리재귀버전
# def remove(x,xs):
#     def loop(x,xs):
#         if x not in xs:
#             return xs
#         else:
#             a=xs.partition(str(x))
#             xs=a[0]+a[2]
#             return loop(x,xs)
#     return loop(x,xs)
# # 테스트 케이스
# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))
# # for루프
# def remove(x,xs):
#     count = 0
#     for i in range(len(xs)):
#         if x==xs[i]:
#             count +=1
#     for i in range(count):
#         a=xs.partition(str(x))
#         xs=a[0]+a[2]
#     return xs
# # 테스트 케이스
# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))
# # while 루프 함수
# def remove(x,xs):
#     while x in xs:
#         a=xs.partition(str(x))
#         xs=a[0]+a[2]
#     return xs
# # 테스트 케이스
# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))



#실습10=================================================



# # #실습11 리스트(1)
# def drop_before(s,index):
#     while(index>0):
#         s=s[1:]
#         index-=1
#     return s
# # s = [1,2,3,4,5]
# print("drop_before(s,0) =", drop_before(s,0))
# print("drop_before(s,1) =", drop_before(s,1))
# print("drop_before(s,2) =", drop_before(s,2))
# print("drop_before(s,3) =", drop_before(s,3))
# print("drop_before(s,4) =", drop_before(s,4))
# print("drop_before(s,5) =", drop_before(s,5))
# print("drop_before(s,6) =", drop_before(s,6))
# print("drop_before(s,-3) =", drop_before(s,-3))
# print("drop_before([],4) =", drop_before([],4))
#리스트(2) 재귀
# # 재귀 버전
# def take_before(s,index):
#     size=len(s)
#     if s!=[] and index<len(s):
#         if size!=index:
#             size=len(s)-1
#             return take_before(s[:size],index)
#         else:
#             return s
#     else:
#         return s
# s = [1,2,3,4,5]
# print(take_before(s,0))
# print(take_before(s,1))
# print(take_before(s,2))
# print(take_before(s,3))
# print(take_before(s,4))
# print(take_before(s,5))
# print(take_before(s,6))
# print(take_before(s,-3))
# print(take_before([],4))
# #리스트(2) 재귀(2)
# def take_before(s,index):
#     if s!=[] and index>0:
#         return [s[0]]+take_before(s[1:],index-1)
#     else:
#         return []
# s = [1,2,3,4,5]
# print(take_before(s,0))
# print(take_before(s,1))
# print(take_before(s,2))
# print(take_before(s,3))
# print(take_before(s,4))
# print(take_before(s,5))
# print(take_before(s,6))
# print(take_before(s,-3))
# print(take_before([],4))
# # 꼬리재귀 버전
# def take_before(s,index):
#     def loop(s,index,tmp):
#         if s!=[] and index>0:
#             tmp.append(s[0])
#             loop(s[1:],index-1,tmp)
#             return tmp
#         else:
#             return []
#     return loop(s,index,[])
# s = [1,2,3,4,5]
# print(take_before(s,0))
# print(take_before(s,1))
# print(take_before(s,2))
# print(take_before(s,3))
# print(take_before(s,4))
# print(take_before(s,5))
# print(take_before(s,6))
# print(take_before(s,-3))
# print(take_before([],4))
# # while 루프 버전
# def take_before(s,index):
#     tmp=[]
#     while index>0 and s != []:
#         tmp.append(s[0])
#         s=s[1:]
#         index-=1
#     return tmp
# # s = [1,2,3,4,5]
# print(take_before(s,0))
# print(take_before(s,1))
# print(take_before(s,2))
# print(take_before(s,3))
# print(take_before(s,4))
# print(take_before(s,5))
# print(take_before(s,6))
# print(take_before(s,-3))
# # print(take_before([],4))
# ##리스트(3)
# def sublist(s,low,high):
#     if low < 0:
#         low = 0
#     if high < 0:
#         high = 0
#     if low <= high:
#         s=drop_before(s,low)
#         s=take_before(s,high)
#         return s
#     else:
#         return []
# s = [1,2,3,4,5]
# print(sublist(s,0,0))
# print(sublist(s,0,1))
# print(sublist(s,0,2))
# print(sublist(s,0,3))
# print(sublist(s,0,4))
# print(sublist(s,0,5))
# print(sublist(s,0,6))
# print(sublist(s,1,1))
# print(sublist(s,1,2))
# print(sublist(s,1,3))
# print(sublist(s,1,4))
# print(sublist(s,1,5))
# print(sublist(s,1,6))
# print(sublist(s,2,2))
# print(sublist(s,2,3))
# print(sublist(s,2,4))
# print(sublist(s,2,5))
# print(sublist(s,2,6))
# print(sublist(s,3,3))
# print(sublist(s,3,4))
# print(sublist(s,3,5))
# print(sublist(s,3,6))
# print(sublist(s,5,2))
# print(sublist(s,-3,-2))



# #실습12 streak===========================================
def longest_streak1(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    index = 1
    for n in s[1:]:
        pass # 이 부분을 채워 넣자.
        index += 1
    return leader, streak_record, leader_index

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak1(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0)
# # => ('0', 3, 15)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1)
# # => ('5', 4, 15)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2)
# # => ('8', 2, 19)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3)
# # => ('8', 3, 2)



# #실습 13 중첩리스트 정수확인
# def count_the(x,xss):
#     count=0
#     for i in range(len(xss)):
#         if isinstance(xss[i],list):
#             count+=count_the(x,xss[i])
#         else:
#             if x == xss[i]:
#                 count+=1
#     return count
# print(count_the(1,[])) #0
# print(count_the(7,[1,7,7])) #2
# print(count_the(7,[1,[7],7])) #2
# print(count_the(7,[7,[2,7,[4,7]]])) #3
# print(count_the(7,[[[[[[],[[7,2,7]],7]]]]])) #3
# print(count_the(7,[[[[7]],[7]],5,7,[3]]))#3
# print(count_the(5,[1,[5,2],[[3],[5,4]],[[[5,5,5,5]]],6,[5,[[5],[[9]]]]])) #8



# #실습 14 중첩리스트 짜부시키기
# def flatten(xss):
#     flat = []
#     for i in range(len(xss)):
#         if xss[i]==[]:
#             continue
#         if isinstance(xss[i],list):
#             flat=flat+flatten(xss[i])
#         else:
#             flat.append(xss[i])
#     return flat
# print(flatten([]))
# print(flatten([1,2,3]))
# print(flatten([1,[],3]))
# print(flatten([1,[1,2,[3,4]]]))
# print(flatten([[[[[[[[1,2,3]]]]]]]]))
# print(flatten([[[[3]],[4]],5,6,[7]]))
# print(flatten([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]]))



# #실습 15 부분문자열
# def substrings_of_length(k,s):
#     if k == 0:
#         return ['']
#     elif 0 < k <= len(s):
#         subs = []
#         for i in range(len(s)-k+1):
#             subs.append(s[i:i+k])
#         return subs
#     else:
#         return None
# TEST CASES
# print(substrings_of_length(0,"ERICA"))
# print(substrings_of_length(1,"ERICA"))
# print(substrings_of_length(2,"ERICA"))
# print(substrings_of_length(3,"ERICA"))
# print(substrings_of_length(4,"ERICA"))
# print(substrings_of_length(5,"ERICA"))
# print(substrings_of_length(6,"ERICA"))
# RESULTS
# ['']
# ['E', 'R', 'I', 'C', 'A']
# ['ER', 'RI', 'IC', 'CA']
# ['ERI', 'RIC', 'ICA']
# ['ERIC', 'RICA']
# ['ERICA']
# None

# #15-(2)
# def substrings(s):
#     result=[]
#     for k in range(len(s)):
#         result+=substrings_of_length(k,s)
#     return result
# print(substrings("ERICA"))
# print(substrings(""))
# RESULTS
# ['', 'E', 'R', 'I', 'C', 'A', 'ER', 'RI', 'IC', 'CA', 'ERI', 'RIC', 'ICA', 'ERIC', 'RICA', 'ERICA']
# ['']

# # #실습 16 오르막리스트(1)
# def ascending(ns):
#       if len(ns) <= 1:
#             return False
#       else:
#             front = ns[0]
#             for n in ns[1:]:
#                   if front >= n:
#                         return False
#                   front = n
#             return True
# print(ascending([1,3]))
# print(ascending([2,3,6,8,12,17]))
# print(ascending([]))
# print(ascending([2]))
# print(ascending([3,3,3,3,3]))
# print(ascending([1,2,2,3]))
# print(ascending([2,3,1]))
# #오르막리스트#2 부분리스트
# def get(k,ns):
#       subs = []
#       for i in range(len(ns)-k+1):
#             subs.append(ns[i:i+k])
#       return subs

# print(get(0,[1,2,3,4,5,6,7]))
# print(get(1,[1,2,3,4,5,6,7]))
# print(get(2,[1,2,3,4,5,6,7]))
# print(get(3,[1,2,3,4,5,6,7]))
# print(get(4,[1,2,3,4,5,6,7]))
# #오르막리스트#3
# def ascending_sublists(ns):
#       ascs = []
#       for sub in sublists(ns):
#             if ascending(sub):
#                   ascs.append(sub)
#       return ascs
# print(sublists([1,5,3,4,8,2,3,5]))
# print(ascending_sublists([1,5,3,4,8,2,3,5]))
# #오르막리스트#4
# def longest_ascending_sublist(ns):
#     if ns != []:
#         longest = []
#         current = [ns[0]]
#         for n in ns[1:]:
#             if current[-1] < n:
#                 current.append(n)
#             else:
#                 if len(longest) < len(current):
#                     longest = current
#                 current = [n]
#         return longest
#     else:
#         return []
#오르막리스트#5
def longest_steepest_ascending_sublist(ns):
    def slope(ns):
        return (ns[-1] - ns[0]) / len(ns)
    if ns != []:
        longest = []
        steepest = 0
        current = [ns[0]]
        longest_ascending_sublist(ns)


        return longest
    else:
        return []

# TEST CASES
print(longest_steepest_ascending_sublist([1,5,3,4,8,2,3,5]))
print(longest_steepest_ascending_sublist([]))
sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
print(longest_steepest_ascending_sublist(sample))

# RESULTS
# [3, 4, 8]
# []
# [7, 23, 34, 67, 77]

# #실습17 소수하고 나하고(1)
# def is_prime(n):
#     if n < 2:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
#소수(2)
# def primes_less_than(n):
#     result=[]
#     for i in range(n):
#         if is_prime(i):
#             result.append(i)
#     result.sort()

#     return result
# print(primes_less_than(2))
# print(primes_less_than(3))
# print(primes_less_than(10))
# print(primes_less_than(30))
#소수(3)
# def primes(k):
#     result=[]
#     i=0
#     while len(result)!=k:
#         if is_prime(i):
#             result.append(i)
#         i+=1
#     return result
# print(primes(0))
# print(primes(1))
# print(primes(5))
# print(primes(10))
# #소수(4)
# def twin_primes(k):
#     result=[]
#     first=2
#     second=3
#     while k>0:
#         if is_prime(n):
#             if second-2==first:
#                 twin=(first,second)
#                 result.appned(twin)
#                 k-=1
#             first=second
#         second+=2
#     return result

    
# print(twin_primes(0))
# print(twin_primes(1))
# print(twin_primes(5))
# print(twin_primes(10))

# #실습18 진법변환(1)
# import math
# def bin2dec(bin):
#     length = len(bin)
#     dec = 0
#     for i in range(length):
#         tmp=int(bin[-(i+1)])
#         if tmp!=0:
#             dec+=(2*tmp)**i      
#     return dec
# print(bin2dec('0')) # 0
# print(bin2dec('1')) # 1
# print(bin2dec('110')) # 6
# print(bin2dec('10011')) # 19
# print(bin2dec('101010')) # 42
# #진법변환(2)
# def dec2bin(dec):
#     bin = ''
#     while not (dec == 0 or dec == 1):
#         mod=dec%2
#         dec=dec//2
#         bin+=str(mod)
#     bin = str(dec) + bin
#     return bin

# print(dec2bin(0))# '0'
# print(dec2bin(1)) # '1'
# print(dec2bin(6)) # '110'
# print(dec2bin(19)) # '10011'
# print(dec2bin(42)) # '101010'