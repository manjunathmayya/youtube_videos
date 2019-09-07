import config
from ftplib import FTP
from tqdm import tqdm
import os


ftp = FTP(config.host_ip)
ftp.login(user=config.username, passwd = config.password)

ftp.cwd('/hd/manjunath/')
print("logged in and pointing to manjunath\n")


filename = "E:\\Manjunath\\youtube\\progress_bar\\telegram.txt"
filesize = os.path.getsize(filename)


#ftp.storbinary('STOR telegram.txt', open(filename, 'rb'))

with tqdm(desc = 'Uploading......', total = filesize) as tqdm_instance:
    
    ftp.storbinary('STOR telegram.txt', open(filename, 'rb') , 
                       2048, 
                       callback = lambda sent: tqdm_instance.update(len(sent))
                   )

print("\nUpload done")


ftp.quit()
