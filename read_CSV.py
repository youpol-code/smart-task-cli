import pandas as pd

df =pd.read_csv("patients.csv")

df["bmi"] =df["weight"] /(df["height"] ** 2)
obese_people = df[df["bmi"]>=30]
print("รายชื่อคนอ้วน (จากไฟล์ CSV):")
print(obese_people)