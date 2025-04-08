import configparser

config = configparser.ConfigParser()
config.read("..\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def GetApplicationURL():
        url = config.get("common info", "baseurl")
        return url