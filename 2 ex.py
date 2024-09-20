import re

input_string = """***/Test/files/1.xls, ***/Test/files/2.XLSX, ***/Test/files/9.vra, 
***/Test/files/3.jpg, ***/Test/files/4.xml, ***/Test/files/5.png, 
***/Test/files/6.xlsm, ***/Test/files/7.xlso, ***/Test/files/8.xls*, 
***/Test/files/9.xlasx, ***/Test/files/9.vba"""

excel_formats_pattern = r'[^,\s]+\.xls[xm]*|\.xls\*|\.xlam'

matches = re.findall(excel_formats_pattern, input_string, re.IGNORECASE)

result = ', '.join(matches)
print(result)
