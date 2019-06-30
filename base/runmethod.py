import requests
import json

class RunMethod(object):
    def post_main(self,url,data=None,header=None):
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res
    
    def get_main(self,url,data,header):
        if header != None:
            res = requests.get(url=url,params=data,headers=header).json()
        else:
            res = requests.get(url=url,params=data).json()
        return res

    def run_main(self,method,url,data,header):
        if method == 'POST' or 'post':
            res = self.post_main(url,data=data,header=header)
        elif method == 'get' or 'GET':
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
