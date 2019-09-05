import config
from ftplib import FTP
import os


#domain name or server ip:

ftp = FTP(config.host_ip)
ftp.login(user=config.username, passwd = config.password)

ftp.cwd('/hd/manjunath/')


print("logged in and pointing to manjunath")


filename = 'news.txt'
localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
localfile.close()
print("download done")


filename = r"E:\Manjunath\youtube\ftp\telegram.txt"
ftp.storbinary('STOR '+os.path.basename(filename), open(filename, 'rb'))
print("upload done")


ftp.quit()
