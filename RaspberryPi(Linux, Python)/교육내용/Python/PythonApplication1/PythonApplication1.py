#=========================================
#=============== Python ==================
#=========================================

# 파이썬 : 간단한 프로그램을 만들때 사용

#print("지금이야 키티"); # : 한줄 주석

#==============		문자형		==============
#a = 123			# a는 숫자형으로 바로 설정
#print(type(a))
#a = 100 * 100
#print(a)
#a , b = 9 , 2
#print(a * b)

#==============		리스트		==============
#a,b,c,d = 0,0,0,0
#a = int(input("1번째 숫자 : ")) # input : " "안에 것을 출력
#b = int(input("2번째 숫자 : ")) # int.parse()와 비슷한 역할
#c = int(input("3번째 숫자 : "))
#d = int(input("4번째 숫자 : "))
#hap = a + b + c + d
#print("합계 ==> %d" %hap)

#==============		리스트(배열)		==============
#aa = []
#aa.append(0)
#aa.append(0)
#aa.append(0)
#aa.append(0)
#print(len(aa))				# 리스트 변수의 크기 출력
#print(aa)					# 요소의 값들을 출력
#bb = []
#for i in range(0, 100):		# 반복문 for문을 선언
#	bb.append(i)			# i값을 리스트에 요소로 추가
#print(bb)

#==============		리스트(다양한 함수사용)		==============
#aa = [30, 10, 20]
#print("현재의 리스트 : %s" %aa)

#aa.append(40)							 # 추가
#print("append 후의 리스트 : %s" %aa)     
#aa.pop()								 # 삭제
#print("pop 후의 리스트 : %s" %aa)
#aa.sort()								 # 오름차순정렬
#print("sort 후의 리스트 : %s" %aa)
#aa.reverse()							 # 역순
#print("reverse 후의 리스트 : %s" %aa)
#aa.insert(2, 222)						 # 삽입
#print("insert 후의 리스트 : %s" %aa)
#print("20값의 위치 : %d" % aa.index(20)) # 검색
#aa.remove(222)							 # 검색과 삭제
#print("remove 후의 리스트 : %s" %aa)
#aa.extend([77,88,77])					 # 확장
#print("extend 후의 리스트 : %s" %aa)
#print("77값의 개수 : %d" % aa.count(77))

#==============		리스트(2차원 배열)		==============
#aa = [[1,2,3,4],
#	  [5,6,7,8],
#	  [9,10,11,12]]
#print(aa[0][0])
#print(aa[0])
#print(aa[1][2])
#print(aa)

##==============		  튜플 (읽기전용 리스트)	 	==============
#str = "파이썬 문자열"
#print(str[0])
#print(str[-1])						# 뒤에서 첫번째 수 출력
##str[-1] = '렬'						# 오류 (튜플은 한번 선언된 요소 값은 수정 불가능)
#card = 'red', 4, 'python', True
#print(card)
#print(card[1])
##card[0] = 'blue'

#bb = [1, "apple"]
#print(bb)

##==============		튜플(값을 변수로 리턴)		==============
# 값을 바꾸지 못함 (ex : 첫번째 red를 card[0] = 'blue' 로 하면 에러)
#card = 'red', 4 , 'python', True
#a, b, c, d = card
#print(a)
#print(b)
#print(c)
#d = False
#print(d)

#==============		딕셔너리		==============
#dict = {'번호':10, '성명':'장동건', '나이':23, '사는곳':'서울'}

#print(dict)
#print(type(dict))
#print(dict['나이'])
#dict['나이'] = 24
#print(dict['나이'])
#dict['직업'] = '배우'
#print(dict)
#print(dict.keys())		# 왼쪽 key
#print(dict.values())	# 오른쪽 value
#print('사는곳' in dict) # 사는곳이란 key값이 있느냐? (t)
#del dict['사는곳']		# 사는곳이란 key값을 지워라
#print('사는곳' in dict) # 사는곳이란 key값이 있느냐? (f)
#print(dict)

#==============		if문		==============
#a = 23
#if a < 50:
#	print('50보다 작군요')
## if else
#if a < 20:
#	print('20보다 작군요')
#else:
#	print('20보다 크군요')
## elif
#age = int(input('현재 나이를 입력합니다. '))
#if	 age < 10:
#		print('유년층입니다.')
#elif age < 20:
#		print('10대입니다.')
#elif age < 30:
#		print('20대입니다.')
#elif age < 40:
#		print('30대입니다.')
#else:
#		print('장년층입니다.')

#==============		for문		==============
#for i in range(0, 5, 1): # range() 범위안에서
#	print(i)
#print("---------")
#for j in[1,3,5,7,9]:
#	print(j)
#print("---------")
#for k in(0, 3, 1):
#	print("꿈은 이루어 진다.")

#==============		for문(2)		==============

##for문을 활용하여 1에서 10까지 합을 구하시오.
#sum = 0
#for i in range(1, 11, 1):
#	sum = sum + i
#print("sum : %d" %sum)
#print("---------")

##for문을 활용하여 1에서 10까지 식과 합을 구하시오.
#sum = 0
#for j in range(1, 11, 1):
#	if j < 10:
#		print("%d + " %j, end="")
#	elif j == 10:
#		print("%d = " %j, end="")
#	sum = sum + j
#print("%d" % sum)

#==============		while문		==============
#str = "꿈은 이루어 진다."
#i = 0
#while i<3:
#	print(str)
#	i = i + 1
#print("-----------------------------")
##while문으로 입력한 숫자만큼 str을 반복 출력하시오.
#i = int(input("반복 횟수 숫자를 입력합니다 : "))
#j = 1
#flag = True
#while flag:
#	j = j + 1
#	if i<j:
#		flag = False
#	print(str)

#==============		break문		==============
##for문,break문을 활용하여 1에서 20까지 합이 100보다 가장 가깝고 작은 합을 구하시오.
#sum , i = 0, 0
#for i in range(1, 20, 1):
#	sum+=i
#	if sum>100:
#		break
#sum-=i
#print("%d" %sum)
#print("------------------------")
##while문,break문을 활용하여 입력한 1에서 숫자만큼 합을 구하시오.
#sum, i = 0, 0
#j = int(input("숫자를 입력합니다."))
#while True:
#	if i<j:
#		i = i + 1
#		sum+=i
#	elif i == j:
#		break
#print("1에서 %d까지의 합은 %d입니다." % (j, sum))

#==============		continue문		==============
#i = 0
#while i < 100:		# i가 100보다 작을 때 반복. 0부터 99까지 증가하면서 100번 반복
#  i += 1			# i를 1씩 증가시킴
#  if i % 2 == 0:	# i를 2로 나누었을 때 나머지가 0이면 짝수
#    continue		# 아래 코드를 실행하지 않고 건너뜀
#  print(i)

#==============		 구구단 (4~7출력)	==============

#for i in range(1, 10, 1):
#	b = 4 * i
#	print ("4 x %d = %d" %(i,b))

#for i in range(1, 10, 1):
#	for j in range(1, 10, 1):
#		if 4 > i:
#			break
#		if 7 < i:
#			break
#		print("%d * %d = %d" %(i, j , (i*j)))

#for i in range(4, 8, 1):
#	for j in range(1, 10, 1):
#		print("%d * %d = %d" %(i, j, i*j))

#==============		윤년 계산		==============

# 윤년  ==	4로 나누어지면서 100으로 나누어지지않는 년도 , 400으로 나누어 떨어지는 년도
# 평년	==	나머지 

#print("=================================")
#print("============윤년계산=============")
#print("=================================")
#print("")

#Year = int(input("년도를 입력해주세요 : "))

#if(Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0):
#	print(Year,"년은 윤년입니다.")
#else:
#	print(Year,"년은 평년입니다.")

#==============		Random Choice		==============

#Menu = "거북이동네", "굽네치킨", "오매족", "구워삶기", "롤링파스타", "개미집", "개성상인", "맥도날드"
#import random
#print("=================================")
#print("   오늘의 메뉴는 : ", random.choice(Menu))
#print("=================================")

#==============		Random Game		==============

#import random

#LuckyNumber = random.randint(1,46)

#print("==========================================")
#Number = int(input("1 ~ 45 중에서 번호를 선택하세요 : "))
#print("==========================================")
#print("★★★★★ 행운의 번호는 :", LuckyNumber, " ★★★★★")
#print("==========================================")
#if Number == LuckyNumber:
#	print("축하합니다 !! 당첨되었습니다 !! 당첨금은 100,000,000입니다.")
#else:
#	print("아쉽네요... 다음 기회를 노립시다 !!")
#print("==========================================")


#==============		Lotto		==============
#1등 당첨 : 숫자와 순서 동일
#2등 당첨 : 숫자만 동일
#3등 당첨 : 숫자 하나만 동일

#import random

#MyNum = eval(input("1~ 45 중에 번호를 선택해주세요 : "))

#LukNum = 13 # 행운번호 설정
#print("행운의 번호는", LukNum)
#i = LukNum // 10
#j = LukNum % 10

#if i == MyNum // 10 and j == MyNum % 10:
#	print("1등 당첨입니다 !! 당첨금 : 50,000,000")
#elif i == MyNum % 10 and j == MyNum // 10:
#	print("2등 당첨입니다 !! 당첨금 : 10,000,000")
#elif (i == MyNum % 10 or \
#		i == MyNum // 10 or \
#		j == MyNum % 10 or \
#		j == MyNum // 10) :
#		print("3등 당첨입니다 !! 당첨금 : 5,000,000")

#else:
#	print("아쉽네요... 다음 기회를 노립시다 !")