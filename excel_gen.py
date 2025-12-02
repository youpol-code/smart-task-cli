from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from typing import cast 

def create_report() -> None:
    wb: Workbook = Workbook()

    ws: Worksheet = cast(Worksheet,wb.active)
    ws.title ="My Report"

    headers =["รายการสินค้า","ราคา (บาท)","จำนวน (ชิ้่น)"]
    ws.append(headers)

    data = [
        ["คีย์บอร์ดไร้สาย",1500,2],
        ["เมาส์เพื่อสุขภาพ",950,5],
        ["แผ่นรองเมาร์",120,10]
    ]

    for row in data:
        ws.append(row)
    
    filename="report_output.xlsx"
    wb.save(filename)
    print(f"สร้างไฟล์ {filename} เรียบร้อยแล้ว!")

if __name__ =="__main__":
    create_report()