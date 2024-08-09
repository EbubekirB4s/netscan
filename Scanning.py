import socket
import sys
try:  
    def normalScan(ip):

        for port in range(134,136):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            result = s.connect_ex((socket.gethostbyname(ip),port))
            if(result==0):
                print('port is opened', port)
           
            s.close()
except socket.error as e:
    print(e)
    sys.exit()
