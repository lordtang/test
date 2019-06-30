#coding:utf-8
import json

class OperationJson(object):
    '''
    功能：操作json文件
    参数：json文件路径
    '''
    def __init__(self,path=None):
        __default_path = "./new.json"
        if path:
            self.path = path
        else:
            self.path = __default_path
    def read_data(self):
        with open(self.path,'r') as fp:
            data = json.load(fp)
            return data

    def get_value_by_key(self,key):
        json_data = self.read_data()

        if type(json_data) == list:
            # 处理json是一个list的情况
            for d in json_data:
                for k,v in d.items():
                    if k==key:
                        return v

        if type(json_data) == dict:
            # 处理json是一个dict的情况
            data = json_data[key]
            return data

if __name__ == "__main__":    
    json_obj = OperationJson()
    r = json_obj.get_value_by_key("k")
    print(r)