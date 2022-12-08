# 对request进行二次封装

import requests


class HttpClient:
    # 只要用到这个类，就会进入到init这个函数里去
    def __init__(self):
        self.session = requests.session()

    def send_request(self, method, url, param_type, data, **kwargs):
        # 请求方式转为大写
        method = method.upper()
        # 数据类型转为大写
        param_type = param_type.upper()
        # 判断post还是get
        if 'GET'==method:
            response = self.session.request(method=method, url=url, data=None, **kwargs)
        elif 'POST'==method:
            if param_type == 'FROM':
                # 如果是表单格式
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'DELETE'==method:
            if 'FROM'==param_type:
                # 如果是表单格式
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif method == 'PUT':
            if param_type == 'FROM':
                # 如果是表单格式
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError

        return response

    def close_session(self):
        self.session.close()
