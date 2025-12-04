from fpdf import FPDF

def create_thai_pdf():
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("Sarabun",style="",fname="Sarabun-Regular.ttf")
    pdf.set_font("Sarabun",size=20)

    pdf.cell(w=0,h=10,text="ใบเสนอราคา (Quotation)",new_x="LMARGIN",new_y="NEXT",align="C")

    pdf.set_font("Sarabun",size=16)
    pdf.cell(w=0,h=10,text="ลูกค้า: คุณยอดพล",new_x="LMARGIN",new_y="NEXT")
    pdf.cell(w=0,h=10,text="รายการสินค้า:",new_x="LMARGIN",new_y="NEXT")

    items=["1. คีย์บอร์ดไร้สาย","2. เมาส์เพื่อสุขภาพ","3. จอคอมพิวเตอร์"]
    for item in items:
        pdf.cell(w=0,h=10,text=f"   {item}",new_x="LMARGIN",new_y="NEXT")

    pdf.output("thai_invoice.pdf")
    print("สร้างไฟล์ PDF ภาษาไทยสำเร็จ")

if __name__=="__main__":
    create_thai_pdf()
