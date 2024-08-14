import Scanning
def main():
    return switchdict
    
switchdict = {
}
class Switches:
    def __init__(self, arg, function):
        self.arg=arg
        self.function=function
    def addSwitchsToDict(self):
        switchdict[self.arg] = self.function

scanTDP= Switches('-sT', Scanning.tdpScan)
scanTDP.addSwitchsToDict()

main()
