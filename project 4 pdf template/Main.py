from fpdf import FPDF
import pandas as pd
pdf=FPDF(orientation="P", unit="mm", format="A4" )

df=pd.read_csv("project 4 pdf template\\topics.csv")
for index,row in df.iterrows():
    pdf.add_page()
    
    #Set the header
    pdf.set_font("Times",style="B",size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1,border=0)
    pdf.line(10,21,200,21)
    
    #Set the footer
    pdf.ln(244)
    pdf.set_font(family="Times",style="I", size=10)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    
    for i in range(row["Pages"]-1):
        pdf.add_page()
        
        #Set the footer
        pdf.ln(254)
        pdf.set_font(family="Times",style="I", size=10)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    
        
        
          
pdf.output("output.pdf")

