# -*- coding:utf-8 -*-
import configparser


class GetConf(object):
    """
    获取配置文件,留一个函数做参考
    """

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read("../conf/config.ini", encoding="utf-8-sig")

    def get(self, section, option):
        return self.cf.get(section, option)

    def filepath(self):
        readdict = {
            "rarpath": self.get("filepath", "rarpath"),
            "zippath": self.get("filepath", "zippath"),
        }
        return readdict



