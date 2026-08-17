# Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx, or .txt and print the file type.

filename = input("Enter filename: ")

if filename.endswith(".pdf"):
    print("PDF file")
elif filename.endswith(".docx"):
    print("DOCX file")
elif filename.endswith(".txt"):
    print("TXT file")
else:
    print("Unknown file type")