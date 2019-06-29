#coding:utf-8
import xlrd

class Operation_excel(object):
    def __init__(self,path=None,sheet_id=None):
        default_path = "./memberCount.xlsx"
        if path:
            self.path = path
            self.sheet_id=sheet_id
        else:
            self.path = default_path
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        '''
        功能：获取sheet的内容
        '''
        data = xlrd.open_workbook(self.path)
        tables = data.sheets()[self.sheet_id]
        return tables

    @property
    def lines(self):
        '''
        功能：获取表格总行数
        参数：无
        返回值：行数
        '''
        return self.data.nrows       

    def get_cell_value(self,row,col):
        '''
        功能：获取表格中某个位置的数据
        参数：表格的行和列
        返回值：数据
        '''
        return self.data.cell_value(row,col)

if __name__ == "__main__":
    path = "./memberCount.xlsx"
    table = Operation_excel(path,0)
    lines = table.lines
    r = table.get_cell_value(3,3)
    print(r)