import sys
import ipaddress
import socket
import switches

def main():
    getArgs()
    



def getArgs():
    argList=[]
    # return sys.argv >>>> returned an object exp. ['.\\main.py', '-a']
    
    if(len(sys.argv)==1):
        print("please enter the an ıp adress for scan")
    else:
        
        argLength = len(sys.argv)-1
        for i in range(1,len(sys.argv)):
            argList.append(sys.argv[i])
        argControl(argList)
           
def argControl(argList):
    for i in range(0,len(argList)):
        print(switches.switchdict)
        # if(argList[i] in switches.switchdict):
        #     return argList[i]
            

def controlIpAdress(ip):
    try:
        ip= ipaddress.ip_address()
    except ValueError:
        print('The Ip Adress is not found')
main()