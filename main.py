import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    print(filepath)
    df = pd.read_excel(filepath)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_ne = filename.split('-')[0]
    print(filename)
    print(invoice_ne)
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{invoice_ne}')
    pdf.output(f"PDFs/{filename}.pdf")

    print(df)

