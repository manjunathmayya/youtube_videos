import zipfile
import os


''' Zip files in folder news to testzip.zip  '''

folder_to_be_zipped = 'news'

with zipfile.ZipFile('testzip.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
    for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
        for file in files:
            newzip.write(os.path.join(dirpath, file))
    


''' Unzip files from testzip.zip to new_unzipped  '''
    
folder_to_be_unzipped = 'news_unzipped'

with zipfile.ZipFile('testzip.zip', 'r') as zip_ref:
    zip_ref.extractall(folder_to_be_unzipped)
