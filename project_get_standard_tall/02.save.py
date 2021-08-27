"""
pip install lxml
conda install -c conda-forge pandas
conda install -c conda-forge beautifulsoup4
"""

import sqlite3
import pandas as pd


# db연결
con = sqlite3.connect("standard_tall.db")

# 남자
df_boy = pd.read_html("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/bmiCalcurator.do?menu_no=3071&menu_grp=MENU_NEW03", header=1)[0]
df_boy = df_boy.rename(columns={"연령(세)": "age", "저체중": "level1", "정상체중": "level2", "과체중": "level3", "비만": "level4"})
df_boy.to_sql("boy", con)


# 여자
df_girl = pd.read_html("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/bmiCalcurator.do?menu_no=3071&menu_grp=MENU_NEW03", header=1)[1]
df_girl = df_girl.rename(columns={"연령(세)": "age", "저체중": "level1", "정상체중": "level2", "과체중": "level3", "비만": "level4"})
df_boy.to_sql("girl", con)

con.close()
