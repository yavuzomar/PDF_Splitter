from pdfrw import PdfReader, PdfWriter
from tkinter import *
from tkinter.filedialog import askopenfilename
import os

def selectPDF():
    global PDFpages
    filename= askopenfilename(filetypes=[("PDF Files", "*.pdf")], initialdir=os.getcwd())
    PDFpages=PdfReader(filename).pages
    lPage.set(len(PDFpages))
    PDFfile.set(filename)

def splitPDF():
    try:
        outFile=PdfWriter(f'{os.path.basename(PDFfile.get()).split(".")[0]}_{fPage.get()}-{lPage.get()}.pdf')
        for pNumber in range(fPage.get(), lPage.get() + 1):
            outFile.addpage(PDFpages[pNumber-1])
        outFile.write()
    except:
        return
    os.startfile(os.getcwd())

window=Tk()
window.geometry("480x160")
window.resizable(False, False)
window.title("PDF Splitter 1.0")

btnSelect = Button(window, width=12, font=("Arial",11), text="Select PDF", command=selectPDF)
btnSelect.grid(row=0, column=0, padx=30, pady=30, sticky=W)
PDFfile=StringVar()
txtPDF = Entry(window, width=25, font=("Arial",14), bd=2, state="disabled", textvariable=PDFfile)
txtPDF.grid(row=0, column=0, padx=160, pady=30, sticky=W)

lblPages = Label(window, font=("Arial",14), text="Pages:")
lblPages.grid(row=1, column=0, padx=30, pady=10, sticky=W)
fPage=IntVar(window, value="1")
txtFirstPage = Entry(window, width=3, font=("Arial",14), bd=2, textvariable=fPage)
txtFirstPage.grid(row=1, column=0, padx=100, pady=0, sticky=W)
lblBetween = Label(window, font=("Arial",14), text="-")
lblBetween.grid(row=1, column=0, padx=140, pady=10, sticky=W)
lPage=IntVar(window, value="")
txtLastPage = Entry(window, width=3, font=("Arial",14), bd=2, textvariable=lPage)
txtLastPage.grid(row=1, column=0, padx=157, pady=0, sticky=W)

btnSplit = Button(window, width=12, font=("Arial",12), text="Split PDF", command=splitPDF)
btnSplit.grid(row=1, column=0, padx=300, pady=10, sticky=W)

window.mainloop()