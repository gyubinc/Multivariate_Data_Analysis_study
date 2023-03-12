def fahrenheit(cel):
    return ((9/5)*cel+32)


print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다")
celcius = float(input('변환하고 싶은 섭씨 온도를 입력해 주세요: '))
print(f'섭씨온도 : {celcius}')
print(f'화씨온도 : {fahrenheit(celcius):.2f}')

