class Logger:
    class Levels:
        Info = 0
        Warning = 1
        Error = 2
        Success = 3

    class Colors:
        infocolor = '\033[96m'
        warningcolor = '\033[91m'
        successcolor = '\033[92m'
        errorcolor = '\033[91m'
        default = '\033[0m'
    
    def log(self, level, message):
        if level == self.Levels.Info:
            print(self.Colors.infocolor  + "[INFO]" + self.Colors.default + " " + message)
        if level == self.Levels.Error:
            print(self.Colors.errorcolor + "[ERROR]" + self.Colors.default + " " + message)
        if level == self.Levels.Warning:
            print(self.Colors.errorcolor + "[WARNING]" + self.Colors.default + " " + message + self.Colors.errorcolor + " [WARNING]" + self.Colors.default)
        if level == self.Levels.Success:
            print(self.Colors.successcolor + "[SUCCESS]" + self.Colors.default + " " + message)