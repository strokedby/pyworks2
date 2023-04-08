점수 = 75
if 점수 >= 60:
    print ("합격")
else :
    print ("합격")
    
#좌석배치
customer = 23 #입장객
col_num = 5 #좌석 열
#row_num 0; #줄수

if customer % col_num == 0 :
    row_num = int (customer / co_num)
else : row_num = int (customer / col_num) + 1
print (row_num)

#print (str (row_num)) + "줄이 필요합니다."
#print (f'{ronw_num} 줄이 필요합니다.')
#print ("{}줄이 필요합니다.".format(row_num))

for i in range (0, row_num) :
    for j in range(1, col_num+1):
    #좌석번호가 고객번호가 클때 빠져나옴
    seat_num = (col_num * i) + j
    if seat_num = (col_num * i) + j
       break
    #print ("좌석" + str (seat_num)), end=' ')
    print (f '좌석 (seat_num)' + str (seat_num, end='  '))
     print()
