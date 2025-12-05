from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "API พร้อมทำงาน"}

@app.get("/calculate")
def calculate(x:int,y:int):
    return {"result": x +y}

@app.get("/get-invoice")
def get_invoice(name: str,price: int):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("Sarabun",style="",fname="Sarabun-Regular.ttf")
    pdf.set_font("Sarabun",size=25)

    pdf.cell(text="ใบเสร็จรับเงิน (Receipt)",w=0,h=20,align="C",new_x="LMARGIN",new_y="NEXT")

    pdf.set_font("Sarabun",size=16)
    pdf.cell(text=f"ลูกค้า: {name}",w=0,h=10,new_x="LMARGIN",new_y="NEXT")
    pdf.cell(text=f"ยอดชำระ: {price:,} บาท",w=0,h=10,new_x="LMARGIN",new_y="NEXT")
    pdf.cell(text=f"ขอบคุณที่ใช้บริการ!",w=0,h=10,new_x="LMARGIN",new_y="NEXT")

    filename = "api_invoice.pdf"
    pdf.output(filename)

    return FileResponse(filename,media_type='application/pdf',filename=f"invoice_{name}.pdf")
