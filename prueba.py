import jinja2
import pdfkit
from datetime import datetime

#pdfkit.from_string("hello world", "string.pdf")
pdfkit.from_file("index.html","file.pdf")