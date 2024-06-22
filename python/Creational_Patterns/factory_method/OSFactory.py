from IOS import IOS
from AndroidOS import Android
from WindowsOS import WindowsOS
from OS import OS

class OSFactory:
    def get_instance(self, os: str ) -> OS:
        if os == 'IOS':
            return IOS()
        elif os == 'Android':
            return Android()
        elif os == 'Windows':
            return WindowsOS()
        else:
            return None