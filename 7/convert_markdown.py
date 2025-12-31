import markdown
import pdfkit

with open("input.md", "r") as f:
    md_text = f.read()

html_text = markdown.markdown(md_text)

with open("input.html", "w") as f:
    f.write(html_text)

path_wkhtmltopdf = r'C:\Users\biton\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

pdfkit.from_file("input.html", "output.pdf", configuration=config)
