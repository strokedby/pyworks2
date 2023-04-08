#날짜 시간 관련 모듈
import datetime

#오늘의 날짜와 시간
now = datetime.datetime.today ()
print (now)
print (now.strftime)

#날짜 - 년, 월, 일 출력
print ("{}년" .format (now.year))
print ("{}월" .format (now.month))
print ("{}일" .format (now.month))

#시간 = 시, 분, 초
print ("{}시". .format (now.hour))
print ()
