import pandas as pd
from typing import Dict,List,Any

data : Dict[str,List[int | float]] ={
    "weight": [70,100,60,95,50],
    "height": [1.70,1.70,1.65,1.90,1.55]
}

df = pd.DataFrame(data)
df["bmi"] =df["weight"] / (df["height"] **2)
obese_people =df[df["bmi"]>=30]
print("รายชื่อคนอ้วน:")
print(obese_people)