import pytest
import requests

from UcmpApi.com.get_cookie_test import test_get_res_cookie


class Test_Organiztion:
    def test_cre_org(self,test_get_res_cookie):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateOrganization"
        body = {"Description": "", "Name": "test1", "Id": 0, "ParentId": 1, "Source": 1}
        headers = {
                   "Content-Type": "application/json;charset=UTF-8",
            'Accept': 'application/json'

                   }

        res = requests.post(url, data=body, headers=headers, cookies=test_get_res_cookie())
        print(res.json())


if __name__ == '__main__':
    pytest.main(['Organization_test.py'])
