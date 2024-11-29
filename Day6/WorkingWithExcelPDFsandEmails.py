# Chapter 12: Automating Excel, PDFs, and Emails

import openpyxl
from openpyxl.styles import Font
import PyPDF2
import smtplib
from email.message import EmailMessage

# ------------------- Excel Automation -------------------

# Load and Read Excel
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active
print(sheet['A1'].value)  # Read a cell

# Write to Excel
sheet['B1'] = 'Hello, Excel!'
sheet['B1'].font = Font(bold=True, color="FF0000")  # Format text
workbook.save('example_modified.xlsx')

# Iterate through cells
for row in sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=3):
    for cell in row:
        print(cell.value)

# ------------------- PDF Automation -------------------

# Read PDF Text
with open('document.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    print(reader.pages[0].extract_text())  # Extract text from the first page

# Merge PDFs
from PyPDF2 import PdfMerger
merger = PdfMerger()
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.write('merged.pdf')
merger.close()

# Split PDFs
from PyPDF2 import PdfWriter
writer = PdfWriter()
with open('document.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    writer.add_page(reader.pages[0])  # Add first page to new PDF
    with open('split_page.pdf', 'wb') as output_file:
        writer.write(output_file)

# ------------------- Email Automation -------------------

# Setup Email
msg = EmailMessage()
msg['Subject'] = 'Automated Email'
msg['From'] = 'your_email@example.com'
msg['To'] = 'recipient@example.com'
msg.set_content('This is an automated email!')

# Send Email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()  # Start secure connection
    server.login('your_email@example.com', 'your_password')
    server.send_message(msg)
    print("Email sent!")

# Sending HTML Email
msg.add_alternative("""
<html>
    <body>
        <h1>This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

# Attach File to Email
with open('document.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

# Bulk Email Sending
recipients = ['recipient1@example.com', 'recipient2@example.com']
for recipient in recipients:
    msg['To'] = recipient
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)
        print(f"Email sent to {recipient}")
