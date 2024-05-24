class User:
    def __init__(self,username=None,password=None,comment=None):
        self._username=username
        self._password=password
        self._comment=comment 
    @property
    def getUserName(self):
        return self._username
    @property
    def getPassWord(self):
        return self._password
    @property
    def getComment(self):
        return self._comment