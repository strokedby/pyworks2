#문자열을 구분해서 리스트로 생성하는 함수
#split(구분기호)
f="banana grape kiwi";
f=f.split(' ') # 공백으로 구분
print(f)
print(f[1])

#문자를 수정(변경)하는 함수 - replace(변경전, 변경후)
str1 = "hello world"
str1 = str1.replace ("World, "Korea")
print(str1)

# 문자열의 공백 처리 함수 - strip()
str2= "hi, soo"
str2 = str2.strip();
#str2 = str2.lstrip() #왼쪽
print (str2)

# 문자열의 위치를 찾는 함수 - find () 결과가 인덱스로 반환
msg = "hello"
print(msg.find('H')) #0 #대소문자 구분함
print(msg.find('l')) # 첫번째의 l을 찾음 - 2
print(msg.find('k')) # -1 (찾는 문자가 없으면 -1을 반환함)