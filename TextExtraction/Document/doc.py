import docx2txt

file = './demo.docx'

# extract text
text = docx2txt.process(file)

print(text)


# import docxpy

# file = './demo.docx'

# # extract text
# text = docxpy.process(file)

# print(text)


# # extract text and write images in /tmp/img_dir
# text = docxpy.process(file, "/tmp/img_dir")


# # if you want the hyperlinks
# doc = docxpy.DOCReader(file)
# doc.process()  # process file
# hyperlinks = doc.data['links']