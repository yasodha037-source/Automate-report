import pandas as pd
from fpdf import FPDF

# Read Excel data
data = pd.read_excel("data.csv.xlsx")

# Analysis
average_marks = data["Marks"].mean()
topper = data.loc[data["Marks"].idxmax()]

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Marks Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)

for index, row in data.iterrows():
    pdf.cell(0, 10, f"{row['Name']} : {row['Marks']}", ln=True)

pdf.ln(10)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(0, 10, f"Topper: {topper['Name']} ({topper['Marks']})", ln=True)

pdf.output("report.pdf")

print("PDF report generated successfully!")
