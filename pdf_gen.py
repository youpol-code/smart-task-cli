from fpdf import FPDF

def create_pdf():
    pdf= FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica",style="B",size=16)

    pdf.cell(w=0,h=10,text="INVOICE / RECEIPT",new_x="LMARGIN",new_y="NEXT",align="C")

    pdf.set_font("Helvetica",size=12)
    pdf.cell(w=0,h=10,text="Customer: Khun Youpol",new_x="LMARGIN",new_y="NEXT")
    pdf.cell(w=0,h=10,text="Date: 2023-10-25",new_x="LMARGIN",new_y="NEXT")

    pdf.line(x1=10,y1=40,x2=200,y2=40)

    pdf.output("my_first_invoice.pdf")
    print("สร้างไฟล์ PDF สำเร็จเรียบร้อย")

if __name__=="__main__":
    create_pdf()

