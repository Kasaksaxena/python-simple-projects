from fpdf import FPDF
import pandas as pd
pdf=FPDF(orientation="P", unit="mm", format="A4" )


pdf.add_page()

pdf.set_font("Arial",size=12)

pdf.cell(w=0,h=12,txt="Hello There!",align="C",ln=1,border=1)

pdf.output("output.pdf")

