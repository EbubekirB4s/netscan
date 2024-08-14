import csv

portsArr = []
def mostCommonTcpPorts():
      with open('most-common-tcp-ports.csv',mode='r') as file:
            csvFile= csv.reader(file)
            for lines in csvFile:
               
               for port in lines:
                    portsArr.append(int(port))          
      return portsArr

