import pandas as pd
from fpdf import FPDF

def generate_invoice():
    print("กำลังโหลดข้อมูลยอดขาย")
    try:
        df=pd.read_csv("input_sales.csv")
    except FileNotFoundError:
        print("หาไฟล์ input_sales.csv ไม่เจอ โปรดตรวจสอบว่าไฟล์อยุ่ที่เดียวกันไหม")
        return

    df["Total"]=df["Price"] * df["Quantity"]

    pdf=FPDF()
    pdf.add_page()

    pdf.add_font("Sarabun",style="",fname="Sarabun-Regular.ttf")
    pdf.set_font("Sarabun",size=20)

    pdf.cell(text="ใบแจ้งหนี้ / INVOICE",w=0,h=15,align="C",new_x="LMARGIN",new_y="NEXT")

    pdf.set_font("Sarabun",size=14)
    pdf.cell(text="บริษัท ยูพล โค้ดดิ้ง จำกัด",w=0,h=8,new_x="LMARGIN",new_y="NEXT")
    pdf.cell(text="วันที่: 2023-10-26",w=0,h=8,new_x="LMARGIN",new_y="NEXT")
    pdf.line(x1=10,y1=45,x2=200,y2=45)
    pdf.ln(5)

    pdf.set_font("Sarabun",size=14)
    w_item = 90
    w_price = 30
    w_qty = 30
    w_total = 40

    pdf.cell(w=w_item,h=10,text="รายการสินค้า",border=1,align="C")
    pdf.cell(w=w_price,h=10,text="ราคา",border=1,align="C")
    pdf.cell(w=w_qty,h=10,text="จำนวน",border=1,align="C")
    pdf.cell(w=w_total,h=10,text="รวม",border=1,align="C",new_x="LMARGIN",new_y="NEXT")

    grand_total = 0;

    for index,row in df.iterrows():
        item_name=row['Product']
        price = row['Price']
        qty = row['Quantity']
        total= row['Total']

        grand_total += total
        
        pdf.cell(w=w_item,h=10,text=str(item_name),border=1)
        pdf.cell(w=w_price,h=10,text=f"{price:,}",border=1,align="R")
        pdf.cell(w=w_qty,h=10,text=str(qty),border=1)
        pdf.cell(w=w_total,h=10,text=f"{total:,}",border=1,align="R",new_x="LMARGIN",new_y="NEXT")

    pdf.ln(5)
    pdf.set_font("Sarabun",size=16)
    pdf.cell(w=w_item + w_qty,h=12,text="ยอดรวมทั้งสิ้น (Grand Total):",border=0,align="R")
    pdf.cell(w=w_total,h=12,text=f"{grand_total:,} บาท",border=1,align="R",new_x="LMARGIN",new_y="NEXT")

    filename="Final_Invoice.pdf"
    pdf.output(filename)
    print(f"สร้างใบแจ้งหนี้ {filename} เสร็จสมบูรณ์! ยอดเงินรวม: {grand_total:,} บาท")

if __name__=="__main__":
    generate_invoice()