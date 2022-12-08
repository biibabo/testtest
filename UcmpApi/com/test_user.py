
# import requests
import resp as resp
from UcmpApi.com.util import TestRequestsUtil


class Test_resource:

    def testLogin(self):
        resp = TestRequestsUtil.sess.post('https://cmp-fe.ucloud.cn/api/gateway?Action=Login',
                                          json={"AccountId": "admin", "Password": "039b091873fbc2f68abe7723b4ac018d"})

        print(resp.json())
        assert resp.json()['RetCode'] == 0

    def testOrg(self):
        resp = TestRequestsUtil().sess.post('https://cmp-fe.ucloud.cn/api/gateway?Action=CreateOrganization',
                                            json={"Description": "", "Name": "test232", "Id": 0, "ParentId": 1,
                                                  "Source": 1},
                                            headers={'Origin': 'https://cmp-fe.ucloud.cn',
                                                     'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/operation/structure'})
        print(resp.json())
        assert resp.json()['Message'] == 'Success'
