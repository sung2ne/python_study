"""
pip install lxml
conda install -c conda-forge pandas
conda install -c conda-forge beautifulsoup4
"""

import pandas as pd


# 남자
boy = pd.read_html("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/bmiCalcurator.do?menu_no=3071&menu_grp=MENU_NEW03", header=1)[0]
boy = boy.rename(columns={"연령(세)": "age", "저체중": "v1", "정상체중": "v2", "과체중": "v3", "비만": "v4"})
boy["age"] = boy["age"].str.replace("1\)", "")
boy["v1"] = boy["v1"].str.replace("결과 < ", " ")
boy["v2"] = boy["v2"].str.split(" ≤\t결과 < ").str[1]
boy["v3"] = boy["v3"].str.split(" ≤\t결과 < ").str[1]
boy["v4"] = boy["v4"].str.replace(" ≤ 결과", "")

print("남자 표준 성장지표")
print(boy.head(5))

# 여자
girl = pd.read_html("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/bmiCalcurator.do?menu_no=3071&menu_grp=MENU_NEW03", header=1)[1]
girl = girl.rename(columns={"연령(세)": "age", "저체중": "v1", "정상체중": "v2", "과체중": "v3", "비만": "v4"})
girl["v1"] = girl["v1"].str.replace("결과 < ", " ")
girl["v2"] = girl["v2"].str.split(" ≤\t결과 < ").str[1]
girl["v3"] = girl["v3"].str.split(" ≤\t결과 < ").str[1]
girl["v4"] = girl["v4"].str.replace(" ≤ 결과", "")
print("\n여자 표준 성장지표")
print(girl.head(5))
