from pdf2image import convert_from_path

images = convert_from_path(r"D:\Zecser\CV\Abhi resume.pdf", poppler_path=r"D:\Poppler-25.12.0\poppler-25.12.0\Library\bin")
print(len(images))