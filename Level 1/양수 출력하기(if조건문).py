# 숫자를 입력받아 음수와 양수 여부를 출력합니다.
x = int(input("숫자를 적어주세요" ))
y = str(input("이름을 적어주세요" ))

if x > 0 : 
  print("%s가 알아본 %d는 양수" %(y, x))
elif x == 0 : 
  print("영")
else : 
  print("음수")
