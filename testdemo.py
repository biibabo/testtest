import requests

from core.basecase import GetCookie


class TestDemo(GetCookie):
    def testadminorganizations(self):
        r = requests.post('https://cmp-fe.ucloud.cn/api/gateway?Action=GetUserRelatedOrganizations',
                                          json={"AccountId": "admin"},
                                          headers={
                                              'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
                                          'Cookie':self.cookie})
        # 第一个组织
        org = r.json()['Data']['Organizations'][0]['Id']
        print(org)
        print(r.json())
        assert r.json()['Message'] == 'Success'