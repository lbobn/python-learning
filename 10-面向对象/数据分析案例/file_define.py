"""
文件定义的类

文件读取
"""
import json

from data_define import Record


# 抽象类
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据,并保存为Record类型"""
        pass


# 文本文件读取
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list = []
        for line in f.readlines():
            line = line.strip()  # 处理空格换行符
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


# json 数据读取
class JSONFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list
