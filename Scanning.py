import socket
import sys
import mostCommonPorts as mcp

try:  
    def createSocketStream(streamType,timeOutSecond,ip,port):
        s = socket.socket(socket.AF_INET, streamType)
        socket.setdefaulttimeout(timeOutSecond)
        res = s.connect_ex((ip,port))
        
        if(res==0):
            print('port is opened', port)
        # else:
        #     print('port is not oppened', port)  
        s.close()
    def normalScan(ip):
        
        portList = mcp.mostCommonTcpPorts()
        for i in range(0,len(portList)):
            createSocketStream(socket.SOCK_STREAM,3,ip,portList[i])

        
    def tdpScan(ip,port):
        
         createSocketStream(socket.SOCK_STREAM,3,ip,145)
        
    def udpScan(ip,port):
        createSocketStream(socket.SOCK_DGRAM, 3,ip,port)

except socket.error as e:
    print(e)
    sys.exit()()
