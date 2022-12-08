import unittest

import requests

from core.basecase import BaseCase


class TestResourceConfig(BaseCase):
    # 1.组织
    def testadminfirstorg(self):
        r = requests.post('https://cmp-fe.ucloud.cn/api/gateway?Action=GetUserRelatedOrganizations',
                          json={"AccountId": "admin"},
                          headers={
                              'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
                              'Cookie': self.cookie})
        # 第一个组织firstorg
        self.firstorg = r.json()['Data']['Organizations'][0]['Id']
        print(self.firstorg)
        # print(r.json())
        assert r.json()['Message'] == 'Success'

    # 2.ucloud安全组
    #     2.1地域
    def testucloudfirewallregion(self):
        r = requests.post('https://cmp-fe.ucloud.cn/api/gateway?Action=GetRegionZoneInfo',
                          json={
                              "AccountId": 2,
                              "Platform": "ucloud"
                          },
                          headers={
                              'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
                              'Cookie': self.cookie})
        region = r.json()['Data'][2]['Region']

        zone = r.json()['Data'][0]['Zone']
        print(region,zone)
        print(r.json())
        assert r.json()['RetCode'] == 0

        # 2.2配置

    def testucloudfirewallconfig(self):
        r = requests.post('https://cmp-fe.ucloud.cn/api/gateway?Action=GetCreateFirewallConfigs',
                          json={"PlatformId": 1},
                          headers={
                              'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
                              'Origin': 'https://cmp-fe.ucloud.cn',
                              'Cookie': self.cookie})
        print(r.json())
        # 2.2.1优先级
        high = r.json()['Data']['Priority'][0]['Value']
        medium = r.json()['Data']['Priority'][1]['Value']
        low = r.json()['Data']['Priority'][2]['Value']
        # 协议类型
        tcp = r.json()['Data']['Protocol'][0]['Value']
        udp = r.json()['Data']['Protocol'][1]['Value']
        gre = r.json()['Data']['Protocol'][2]['Value']
        icmp = r.json()['Data']['Protocol'][3]['Value']
        # 策略
        accept = r.json()['Data']['RuleAction'][0]['Value']
        drop = r.json()['Data']['RuleAction'][1]['Value']
        print(high, medium, low, tcp, udp, gre, icmp, accept, drop)
        assert r.json()['RetCode'] == 0

