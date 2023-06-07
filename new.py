# -*- coding: utf-8 -*-

import csv

filename = "/Users/yawnpurple/코딩/bool/output/output-v2.csv"  # 파일명을 적절히 변경해주세요.

with open(filename, "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

for row in rows[1:]:  # 2번째 행부터 마지막 행까지 반복
    data = row[6]  # "G" 열 데이터 가져오기
    groups = data.split("-")  # 하이픈을 기준으로 묶음 분리

    b_values = []
    for group in groups:
        values = group.strip().split()  # 묶음에서 공백으로 값을 분리
        b_values.extend([value for value in values if value == "b"])  # "b" 값만 추출하여 리스트에 추가

    unique_b_values = list(set(b_values))  # 중복 제거

    for value in unique_b_values:
        print(value)
