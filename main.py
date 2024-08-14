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
    ip = ''
    for i in range(0,len(args)):
        try:
            ip=ipaddress.ip_address(args[i])
            break
        except:
            ip=''
        
    if(ip==''):
        print('please enter the valid ip adress')
        exit()
    else:
        # print(switches.switchdict)
        
        catchArgsAndControl(args,str(ip))
        
def catchArgsAndControl(args,ip):
    args.remove(ip)
    # print(args)

    for i in range(0,len(args)):
           
            
            for x in switches.switchdict.keys():
                if x in args[i]:
                        switch=args[i]
                        switch=switch.replace(x,"")
                        # print(switch)
                        if(switch==""):
                            print("most common ports scanning.")
                            Scanning.normalScan(str(ip))
                        else:
                            print("success")
                            Scanning.tdpScan(str(ip), int(switch))
            
        

main()
