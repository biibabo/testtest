import requests

from core.config import TestResourceConfig
from core.basecase import GetCookie


class TestCreateResource(GetCookie):
   # 2、创建ucloud安全组
    def testfirewall(self):
        r = requests.post('https://cmp-fe.ucloud.cn/api/gateway?Action=CreateFirewall',
                                          json={"AccountId": 2,
                                                "OrgId": self.firstorg,
                                                "RegionEn": self.region,
                                                "Name": "test02",
                                                "Rules": [{"RuleAction": "ACCEPT",
                                                           "Priority": "HIGH",
                                                           "Protocol": "TCP",
                                                           "DstPort": "1",
                                                           "SrcIP": "0.0.0.0/0"}],
                                                "Platform": "ucloud"},
                                          headers = {
                                                'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
                                                'Cookie': self.cookie})
        print(r.json())
    # 3、创建ucloudVPC子网
    # 4、创建ucloud云主机
