COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"


import os

class ErrorLogger:
    def __init__(self, fileName):
        self.fileName  = fileName
        self.warningLog = []
        self.errorLog = []
    
    def addError(self, errorMessage):
        self.errorLog.append(errorMessage)
    
    def addWarning(self, warningMessage):
        self.warningLog.append(warningMessage)

    def displayReport(self):
        print("Warning:")
        for warning in self.warningLog:
            print(warning)
            #print(COLOR_YELLOW + warning + COLOR_RESET)
        print("Errors:")
        for error in self.errorLog:
            print(error)
            #print(COLOR_RED + error + COLOR_RESET)
    def saveToFile(self):
        parent_dir = os.path.dirname(os.path.dirname(self.fileName))
        fileName = os.path.basename(self.fileName)
        fileName = "logs/"+fileName[0:len(fileName)-4]
        f = open(os.path.join(parent_dir,fileName)+"_logs.txt","w")
        f.write("Warnings:\n")
        for warning in self.warningLog:
            f.write(warning + '\n')
        f.write("Errors:\n")
        for error in self.errorLog:
            f.write(error + '\n')
        f.close()