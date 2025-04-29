import configparser

config = configparser.ConfigParser()
config.read("..\\Configurations\\config.ini")

class ReadConfig:
    def GetApplicationURL() -> str:
        url = config.get("common info", "baseurl")
        return url
    
    def GetUsername() -> str:
        username = config.get("common info","username")
        return username
    
    def GetPassword() -> str:
        password = config.get("common info","password")
        return password
    
    def GetWebsitetitle() -> str:
        title = config.get("common info","websitetitle")
        return title