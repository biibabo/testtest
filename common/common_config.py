from core.basecase import BaseCase


class Testcommon(BaseCase):
    # 获取全部云账号信息
    def test_CloudAccount(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetCloudAccountList"
        data = {"AccountStatus":[0]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/operation/platform',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        print(r.json())
        self.assertEqual(0, r.json()['RetCode'])
