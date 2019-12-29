# -*- coding:utf-8 -*-

import sys
import platform


class InfoCollection(object):

    def collect(self):
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    @staticmethod
    def linux():
        pass


    @staticmethod
    def darwin():
        from plugins.collect_darwin_info import IOSInfo
        return IOSInfo().collect()

    @staticmethod
    def build_report_data(data):
        # 留下一个接口，方便以后增加功能或者过滤数据
        pass
        return data

if __name__ == "__main__":
    i = InfoCollection()
    i.collect()
