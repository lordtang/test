#coding:utf-8
from base.operation_excel import Operation_excel
from base.operation_json import OperationJson
from . import data_config


class GetData(object):
    def __init__(self):
        self.oper_excel = Operation_excel()

    def get_case_lines(self):
        return self.oper_excel.lines

    def get_is_run(self,row):
        col = data_config.get_run()
        run_model = self.oper_excel.get_cell_value(row,int(col))
        if run_model == 'yes':
            return True
        else:
            return False

    def is_header(self,row):
        col = data_config.get_header()
        header = self.oper_excel.get_cell_value(row,int(col))
        if header == 'yes':
            header = data_config.get_header_value()
            return header
        else:
            return None

    def get_request_method(self,row):
        col = data_config.get_method_way()
        request_method= self.oper_excel.get_cell_value(row,int(col))
        return request_method

    def get_request_url(self,row):
        col = data_config.get_url()
        request_url = self.oper_excel.get_cell_value(row,int(col))
        return request_url
    
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.oper_excel.get_cell_value(row,int(col))
        if data:
            return data
        else:
            return None
        
    def get_data_for_json(self,row):
        oper_json = OperationJson()
        request_data = oper_json.get_value_by_key(self.get_request_data(row))
        return request_data

    def get_except_result(self,row):
        col = data_config.get_expect()
        except_result = self.oper_excel.get_cell_value(row,int(col))
        if except_result:
            return except_result
        return None


    
if __name__ == "__main__":
    obj = GetData()
    obj.get_case_lines()