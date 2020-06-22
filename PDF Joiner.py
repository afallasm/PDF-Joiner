#Lista para verificar que haya archivos en la carpeta
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter
path = './Input PDF'
fname = './Output PDF'
 
#que pasa si pongo un archivo txt, ocupo que solo traiga PDF
files = glob.glob(f"{path}/*.pdf") 
if files:
    files.sort()
    for name in files:
        #merge files
        pdf = PdfFileReader(name)
        numero_paginas = pdf.getNumPages() 
        for page in range(numero_paginas):
            p = pdf.getPage(page)
            
else:
    print("no files to merge")