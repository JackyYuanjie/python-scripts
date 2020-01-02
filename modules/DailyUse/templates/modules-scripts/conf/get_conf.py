#-*-coding:utf-8-*-
import configparser


class GetConf(object):
    """
    获取配置文件,留一个函数做参考
    """

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(r"E:\yibot\longhujiaoben\read_xls\conf\config.ini", encoding="utf-8-sig")

    def get(self, section, option):
        return self.cf.get(section, option)

    def readxls(self):
        readxlsdict = {
            "xlspath": self.get("readxls", "xlspath"),
            "sheetname": self.get("readxls", "sheetname"),
            "readhead": self.get("readxls", "readhead"),
        }
        return readxlsdict



