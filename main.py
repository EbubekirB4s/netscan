import sys
import ipaddress
import socket
import switches
import Scanning

def main():
   argControl()
def argControl():
    
    del sys.argv[0]
    args = sys.argv
    if(len(args)==0):
        print("please enter the Ip")
    else:
        controlIpAdress(args=args)
        # for i in range(0,len(args)):
        #     if('.' in args[i]):
        #         print(args[i])
        #     else:
        #         print('its not ip')
        # if(argList[i] in switches.switchdict):
        #     return argList[i]
    

def controlIpAdress(args):
    ip = '192.168.1.33'
    # for i in range(0,len(args)):
    #     try:
    #         ip=ipaddress.ip_address(args[i])
    #         break
    #     except:
    #         ip=''
    # if(ip==''):
    #     print('please enter the valid ip adress')
    # else:
    #    Scanning.normalScan(ip) 
    Scanning.normalScan(ip)
    # Is an IP adress control code below
    # try:
    #     ip= ipaddress.ip_address()
    # except ValueError:
    #     print('The Ip Adress is not found')
    

main()
