import ftplib

ftp = ftplib.FTP('ftp.dlptest.com')
ftp.login('dlpuser', 'eiTqR7EMZD8PwbuRR0Au')

ftp.retrlines('LIST')
with open('local_file.txt', 'rb') as f:
    ftp.storbinary('STOR remote_file.txt', f)
with open('local_file.txt', 'wb') as f:
    ftp.retrbinary('RETR remote_file.txt', f.write)
