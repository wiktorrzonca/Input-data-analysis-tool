COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"


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
        for warning in self.warningLog:
            print(COLOR_YELLOW + warning + COLOR_RESET)
        for error in self.errorLog:
            print(COLOR_RED + error + COLOR_RESET)