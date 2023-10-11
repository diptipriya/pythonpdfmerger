import PyPDF2
from PyPDF2 import PdfWriter
import os

dir_list=os.listdir('./')
merger = PdfWriter()

pdf_list=[]
pdfcount=0


for pdf in range (len(dir_list)):
      
      if  dir_list[pdf].lower().endswith('.pdf') :
            pdfcount+=1
            pdf_list.append(dir_list[pdf])

#sortedpdf
pdf_list.sort()


#listing the pdf files in current directory
for i in range(len(pdf_list)):
    
   print(f" {pdf_list[i]}")

print(pdfcount)
#pdf_merged
pdf_merged=[]

while pdfcount:
   pfile=input("Enter the file  you want to merge  or  press enter  to exit ") 
   #break if press enter
   if pfile == "":
       break
    #check for .pdf file extensions  
   if  not pfile.lower().endswith('.pdf'):
     pfile=input("Please enter valid response  as this file is not .pdf or press enter   to exit ")  
    #check if the file exist in the directory 
   while pfile not in pdf_list :  
      pfile=input("Please enter valid response  this file is not present or press enter   to exit ") 
      if pfile == "":
       break

   #if pfile in pdf_list:
   value=pdf_list.index(pfile)

   if pdf_list[value]  in pdf_merged:
         print("file already meged choose another file")
         value=input("please enter valid response to which file  you want to merge press  enter to exit ") 
   
   file=pdf_list[value]
   pdfFile = open(file, 'rb')
   pdfReader = PyPDF2.PdfReader(pdfFile)


   print(f"The pdf file {pdf_list[value]}  you have choosen has {len(pdfReader.pages)} Pages ")
   #takes value of start page
   startpage=int(input("plese tell the start page  "))
   
   while startpage < 0 or startpage > len(pdfReader.pages) :
        startpage=int(input("plese tell a valid start page "))
         
        if  startpage > 0 and startpage <len(pdfReader.pages):
                     break

          

   #takes the value of end page
   endpage=int(input("plese tell the end page  "))
   
   while (endpage < 0) or (endpage > len(pdfReader.pages)) or (endpage < startpage):
            endpage=int(input("plese tell a valid end page"))
            
            if  endpage > startpage and endpage <len(pdfReader.pages):
                break


   startpage-=1
      
   merger.append(pdf_list[value],(startpage,endpage)) 
   pdf_merged.append(pdf_list[value])
   pdfcount-=1 
   

# Write to an output PDF document
output = open("final.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()


      
