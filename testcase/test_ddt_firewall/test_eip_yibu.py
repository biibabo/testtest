import unittest

from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestEip(BaseCase):
    global resourceid

    @file_data("../../testdata/test_eip/test_eip_ucloud.json")
    def test_createucloudeip(self, EIPInstance, expect_code):
        global resourceid
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateEIP"
        data = {"OrgId": 1,
                "AccountId": 2,
                "Platform": "ucloud",
                "EIPInstance": EIPInstance
                }
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(expect_code, r.json()['RetCode'])
        resourceid = r.json()["Data"]["ResourceId"]

    def test_eip_status(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail"
        data = {"cmpUuid": resourceid, "ResourceType": "eip"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)  # �����ѯ����ӿ�
            print(r.json()['Data']['Status'])
            if r.json()['Data']['Status'] == 1:  # �ж�eip��״̬�Ƿ�Ϊ1
                print('�����ɹ�')
                break


