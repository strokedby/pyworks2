#자료구조 

fruit = ["사과", "바나나", "딸기"]
print(fruit)

fruit2 = {'사과' : '빨강', '바나나', '노랑'}
print(fruit2)
print(fruit2 ['사과'])
for ket, val in fruit2.items():
    print(key, ':', val)


#튜플 - 순서가 있고, 중복 허용, 값의 수정 삭제 불가
t = ('a', 'b', 'c', 'b')
print(t)

#집합- 순서가 없고, 중복 불가
s=set() #빈 집합
s.add ('사과')
s.add ('바나나')
print(s)

s2={'a', 'b', 'c', 'd', 'b'}
print(s2)

say = 'hello'
print(say)

#리스트로 변환
print (liset(a2))
