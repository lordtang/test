#coding:utf-8

class global_val:
    Id = "0"
    url = "1"
    run = "2"
    method_way = "3"
    header = "4"
    case_depend = "5"
    data_depend = "6"
    field_depend = "7"
    data = "8"
    expect = "9"
    result = "10"

# 获取case_id
def get_id():
    return global_val.Id

def get_url():
    return global_val.url

def get_run():
    return global_val.run

def get_method_way():
    return global_val.method_way

def get_header():
    return global_val.header

def get_case_depend():
    return global_val.case_depend

def get_data_depend():
    return global_val.data_depend

def get_field_depend():
    return global_val.field_depend

def get_data():
    return global_val.data

def get_expect():
    return global_val.expect

def get_result():
    return global_val.result

def get_header_value():
    header = {
        "header":"123"
    }
    return header