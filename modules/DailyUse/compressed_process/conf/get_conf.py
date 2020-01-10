# -*- coding:utf-8 -*-
import configparser


class GetConf(object):
    """
    获取配置文件,留一个函数做参考
    """

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read("F:\PythonProject\python-scripts\modules\DailyUse\compressed_process\conf\config.ini", encoding="utf-8-sig")

    def get(self, section, option):
        return self.cf.get(section, option)

    def file_path(self):
        readdict = {
            "rarpath": self.get("filepath", "rarpath"),
            "zippath": self.get("filepath", "zippath"),
            "targzpath": self.get("filepath", "targzpath"),
        }
        return readdict


if __name__=='__main__':
    gc = GetConf()
    print(gc.file_path())
