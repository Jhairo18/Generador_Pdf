import jinja2
import pdfkit
from datetime import datetime

my_name = "Romina Pia"
item1 = "Marin"
item2 = "Angel"
item3 = "Lara"
today_date = datetime.today().strftime("%d %b, %Y")

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}

#I have to know what its is
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'basic-template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

#config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/')
output_pdf = 'pdf_generated.pdf'
pdfkit.from_string(output_text, 'pdf_generated.pdf')