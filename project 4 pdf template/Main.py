from fpdf import FPDF
import pandas as pd
pdf=FPDF(orientation="P", unit="mm", format="A4" )

df=pd.read_csv("project 4 pdf template\\topics.csv")
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times",style="B",size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="C",ln=1,border=0)
    pdf.line(10,21,200,21)
pdf.output("output.pdf")

