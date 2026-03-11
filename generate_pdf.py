from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'AML Mid-Sem Part B Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def md_to_pdf(md_path, pdf_path):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    with open(md_path, 'r') as f:
        for line in f:
            # Simple sanitization for FPDF
            line = line.encode('latin-1', 'replace').decode('latin-1')
            if line.startswith('# '):
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, line[2:].strip(), 0, 1)
                pdf.set_font('Arial', size=11)
            elif line.startswith('## '):
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 10, line[3:].strip(), 0, 1)
                pdf.set_font('Arial', size=11)
            elif line.startswith('### '):
                pdf.set_font('Arial', 'B', 11)
                pdf.cell(0, 10, line[4:].strip(), 0, 1)
                pdf.set_font('Arial', size=11)
            elif line.startswith('- '):
                pdf.multi_cell(0, 8, '  ' + line.strip())
            elif line.strip() == '':
                pdf.ln(2)
            else:
                pdf.multi_cell(0, 8, line.strip())
    
    pdf.output(pdf_path)

if __name__ == "__main__":
    md_to_pdf('partB/report.md', 'partB/report.pdf')
    print("PDF generated at partB/report.pdf")
