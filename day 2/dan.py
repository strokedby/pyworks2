'''
# 구구단
dan=int(input ("단을 입력하세요:"))
for i in range (1, 10):
    #이스케이프 문자 - '/n' (줄바꿈)
    current_val = f'{dan}x{i}={dan*i}) /n'
    result_val += current_val
print (result_val)
     
#중첩 for 문

for i in range (5): #0, 1, 2, 3, 4
    for j in range (5):
        print ('*', end='')
    print() #줄바꿈


for i in range (5): #0, 1, 2, 3, 4
    for z in range (0, i+1):
        print ('*', end='')
    print() #줄바꿈


for i in range (0, 5): #0, 1, 2, 3, 4
    for j in range (0, 5-i):
        print ('*', end='')
    print() #줄바꿈
        
    
#전체 구구단
for i in range (2, 10):
    for j in range (1, 10):
        print (f'{i}x{j}={i*j}')
    print ()
'''

for i in range (0, 4) :
    for j in range (1, 6) :
        num = (5*1)+j
        print (num, end= ' ')
    print ()
