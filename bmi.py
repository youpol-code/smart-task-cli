import sys
def get_valid_number(dataTyype: str,message: str) -> int | float :
    try:
        if dataTyype=="int":
            resultdata = int(input(message))
        elif dataTyype=="float":
            resultdata = float(input(message))
        else:
            return -2
            

        return resultdata
    except ValueError:
        return -1

# def inputWeight() -> int: # return weight is good, return -1=have problem
#     try:
#         weight: int = int(input("กรุณาใส่นำ้หนัก: "))
#         return weight
#     except ValueError:
#         return -1

# def inputHeight() -> float: # return weight is good, return -1=have problem
#     try:
#         height: float =float(input("กรุณาใส่ส่วนสูง: "))
#         return height
#     except ValueError:
#         return -1
    



while True:
    weight =get_valid_number("int","กรุณาใส่นำ้หนัก: ")
    if weight ==-1:
        continue
    elif weight ==-2:
        print("function get_valid_number on weight insert on 'int' !!!")
        sys.exit(1)
    else:
        break

while True:
    height =get_valid_number("float","กรุณาใส่ส่วนสูง: ")
    if height == -1:
        continue
    elif height ==-2:
        print("function get_valid_number on height insert on 'float' !!!")
        sys.exit(1)
    else:
        break


bmi: float = weight /(height * height)
print(f"BMI: {bmi}")

bmi_description: str = "" 

if bmi < 18.5:
    bmi_description="Underweight"
elif bmi < 25:
    bmi_description="Normal weight"
elif bmi < 30:
    bmi_description="Overweight"
else:
    bmi_description="Obesity"

print(f"BMI Description : {bmi_description}")
