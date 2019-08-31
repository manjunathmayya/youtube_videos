import zipfile

search_string = 'verifying'

zip = zipfile.ZipFile('news.zip')

for filename in zip.namelist():

   file = zip.open(filename)

   for line_no, line in enumerate(file, 1):
   
       if search_string.lower() in line.lower():
           print( filename + ' : ' + str(line_no) + ' : ' + line)
