import pandas as pd
from typing import List,Dict,Any
def main():
    data : Dict[str,List[Any]] ={
        "สินค้า": ["คีย์บอร์ด","เมาส์","คีย์บอร์ด","หูฟัง","เมาส์","หูฟัง"],
        "แบรนด์": ["Logitech","Logitech","Keychron","Sony","Razer","Sony"],
        "ราคา": [1500,900,3200,4500,1200,5000],
        "จำนวน": [2,5,1,2,3,1]
    }

    df =pd.DataFrame(data)

    df["ยอดขายรวม"]=df["ราคา"] * df["จำนวน"]
    print("--- ตารางข้อมูลเดิม ---")
    print(df)
    print("-"*30)

    pivot_report =df.pivot_table(index="แบรนด์",values="ยอดขายรวม",aggfunc="sum")
    print("--- สรุปยอดขายตามแบรนด์ ---")
    print(pivot_report)

    with pd.ExcelWriter("sales_anlysis.xlsx") as writer:
        df.to_excel(writer,sheet_name="Raw Data",index=False)
        pivot_report.to_excel(writer,sheet_name="Brand Summary")
    
    print("\n สร้างไฟล์ sales_analysis.xlsx เรียบร้อย")

if __name__=="__main__":
    main()