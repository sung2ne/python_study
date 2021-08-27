"""
1. BMI 지수 : 체중(kg) / 키(m)^2
1. BMI 지수 : 체중(kg) / (키(cm)/100)^2
"""


w = 0
t = 0

# 거듭제곱을 구하는 함수
def pow(v):
    return v**2


# 키 입력
def key_input():
    global w
    global t
    w = int(input("체중(kg)을 입력해주세요 : "))
    t = int(input("키(cm)를 입력해주세요 : "))


# BMI 지수 계산
def cal_bmi():
    global w
    global t
    bmi = w / pow(t / 100)

    if bmi < 18.5:
        print("저체중")
    elif bmi >= 25:
        print("비만")
    else:
        print("정상")
