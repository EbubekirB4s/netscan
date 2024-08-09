import Scanning
def main():
    return ""
switchdict = {
}
class Switches:
    def __init__(self, arg, function):
        self.arg=arg
        self.function=function
    def addSwitchsToDict(self):
        switchdict[self.arg] = self.function
        print(switchdict)
udpScanSwitch = Switches('-sU',Scanning.udpScan)
switchdict[udpScanSwitch.arg] = udpScanSwitch.function
main()