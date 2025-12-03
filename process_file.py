import pandas as pd

def main():
    print("กำลังอ่านไฟล์ input_sales.csv ....")
    df =pd.read_csv("input_sales.csv")
    print(f"อ่านข้อมูลมาแล้ว {len(df)} แถว")
    print(df.head())
    print("-"*30)

    df["Total"] = df["Price"] * df["Quantity"]
    summary =df.pivot_table(index="Brand",values="Total",aggfunc="sum")
    print("สรุปยอดขาย")
    print(summary)

    summary.to_excel("summary_report.xlsx",sheet_name="Sale Summary")
    print("บันทึกไฟล์ summary_report.xlsx เรียบร้อย")

if __name__=="__main__":
    main()