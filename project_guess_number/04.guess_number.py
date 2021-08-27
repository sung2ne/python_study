"""
1. 0 ~ 99 사이의 숫자를 맞추는 게임
2. 프로그램을 실행하면 0 ~ 99 사이의 랜덤 숫자를 생성
3. 사용자가 입력한 숫자가 랜덤 숫자보다 크면 "크다"를 출력
4. 사용자가 입력한 숫자가 랜덤 숫자보다 작으면 "작다"를 출력
5. 사용자가 입력한 숫자와 랜덤 숫자가 같을 경우
 - "맞았다"를 출력
 - 몇번시도만에 맞췄는지를 출력
 - 동작시간(사용자가 맞추는데 까지 걸린 시간) 출력하기
"""

from time import time
from random import randint

class guess:
    def __init__(self):
        self.rand = randint(0, 100)
        self.start_time = time()
        self.count = 0
        print("게임을 시작하지!")

    def check(self, n):
        self.count += 1

        if n < self.rand:
            self.r = "작다"
        elif n > self.rand:
            self.r = "크다"
        else:
            self.r = "맞았다"

        self.t = int(time() - self.start_time)
        return self.r, self.t, self.count


g = guess()
while True:
    try:
        i = int(input("숫자를 입력하세요 : "))
        r, t, c = g.check(i)

        if r == "맞았다":
            print(f"맞았다. 도전: {c}회, 시간: {t}초")
            break
        else:
            print(r)
    except:
        print("(오류!) 0 ~ 99 사이의 숫자를 입력하세요")
        pass
