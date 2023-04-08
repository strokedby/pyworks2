#조건문(if문)
#제한속도가 50이상이면 "속도위반" 아니면 "속도준수"을 출력하기

'''
limit_speed=55
if limit_speed>=50: #55>50 -> True
    print("속도위반") #들여쓰기, 인덴트

#제한속도가 50이상이면 "속도위반, 과태료 10만원" 이고
# 50km 미만이면 "안전준수 속도 준수"

limit_speed = 60
if limit_speed>=50 :
   print ("속도위반, 과태료10만원")
else : #limit_speed < 50
   print ("안전 속도 준수")

'''
   
# 시험점수가 65점 이상이면 "합격", 아니면 "불합격" 판정하기
점수 = 55
if 점수 >= 60 :
    print ("합격")
else :
    print ("불합격")

11 % 2 == 1

# 어떤 수를 짝수와 홀수로 출력하세요
# %를 나머지 연산자
num = 5
if num % 2 == 0 :
    print ("짝수")
else :
    print ("홀수")
