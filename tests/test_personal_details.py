import pytest
from pageObjects.dashboard import Dashboard
from utilities.ReadProperties import ReadConfig
from utilities.utils import *

class TEST_002_personal_details:
    baseurl = ReadConfig.GetApplicationURL()

    def performLogin(self):
        pass