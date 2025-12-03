from typing import List,Dict,TypedDict
class PatientRecord(TypedDict):
    weight: int
    height: float

patients : List[PatientRecord] =[
    {"weight": 70,"height": 1.70},
    {"weight": 100,"height": 1.80},
    {"weight": 60,"height": 1.65},
    {"weight": 95,"height": 1.90},
    {"weight": 50,"height": 1.55},
] 
obesity_count: int = 0
for i,patient in enumerate(patients,1):
    w: int = int(patient["weight"])
    h: float = float(patient["height"])
    bmi : float = w / (h * h)
    if bmi >= 30:
        obesity_count+=1
        print(f"Patient {i}: BMI {bmi:.2f} (Obesity)")

print(f"Total Obesity Patients: {obesity_count}")
print("finish program")
