import mock
'''
功能：模拟mock封装
参数：mock_method:模拟的方法
      request_data:请求的数据
      response_data:响应的数据
      url:请求地址
      method:请求方法
返回值：被mock函数之后的返回值
'''
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res

