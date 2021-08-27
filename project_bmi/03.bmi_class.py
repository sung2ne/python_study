"""
1. BMI 지수 : 체중(kg) / 키(m)^2
1. BMI 지수 : 체중(kg) / (키(cm)/100)^2
"""


class BMI:
    def __init__(self, w=0, t=0):
        self.w = w
        self.t = t

    def setdata(self, w, t):
        self.w = w
        self.t = t

    # BMI 지수 계산
    def cal_bmi(self):
        self.bmi = self.w / (self.t / 100) ** 2

        if self.bmi < 18.5:
            return "저체중"
        elif self.bmi >= 25:
            return "비만"
        else:
            return "정상"


w = int(input("체중(kg)을 입력해주세요 : "))
t = int(input("키(cm)를 입력해주세요 : "))
bmi = BMI()
bmi.setdata(w, t)
print(bmi.cal_bmi())
