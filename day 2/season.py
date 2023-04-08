'''
#리스트의 생성 및 인덱싱
seasons=['봄', '여름', '가을', '겨울']
print (seasons[0])
print (seasons[0-1])

#리스트 출력
print (seasons)

#전체 요소 출력
for i in seasons:
    print (i)

#요소의 개수
    print ("리스트 (배열)의 크기: ", len(seasons))

#요소를 수정
    seasons[1] = 'summer'

print (seasons[1])

#요소 삭제
del seasons[1]
print (seasons)


#리스트의 연산
#합계, 평균, 개수

score = [70,80,50,60,90,40]
count=[len(score)]
sum_v = 0

for i in score:
    sum_v = sum_v+i
    print ('i', i, 'sum_v=', sum_v)
    
avg = sum_v / count

print ("개수:", count)
print ("합계:", sum_v)
print ("평균:", avg)
'''

scorelist = [10,20,30,40]
#요소 추가 (appen()함수 - 맨뒤에 추가됨)
scorelist.append (50)
print (scorelist)

#특정 위치에 요소 추가 (insert(위치변환))
scorelist.insert (2,60)
print (scorelist)

#요소 삭제 (pop()-맨 뒤 요소 삭제)
scorelist.pop()
print(scorelist)

#요소 개수 (len)
print (len(scorelist))
