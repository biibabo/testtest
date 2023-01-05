# -*- coding: UTF-8 -*-
import logging
import time

import polling as polling
import requests
from ddt import ddt, file_data

from core.basecase import BaseCase


# @ddt
class TestCreatevm(BaseCase):
    # @file_data("../../testdata/test_vm/test_vm_ucloud.json")
    # 创建ucloud云主机
    def test_01_WorkflowCreateVM(self):
        # global SerialNum
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=WorkflowCreateVM"
        data = {
            "AccountId": 2,
            "OrgId": 1,
            "Platform": "ucloud",
            "PlatformId": 1,
            "AccountName": "混合云正式账号",
            "VMInstances": [
                {
                    "Id": 1672803465100,
                    "Name": "UHost---",
                    "Count": 1,
                    "RegionEn": "cn-sh2",
                    "ZoneEn": "cn-sh2-01",
                    "MachineType": "OM",
                    "GPUType": "",
                    "CPUPlatform": "Intel/Auto",
                    "GPU": 0,
                    "CPU": 1,
                    "Memory": 2,
                    "Password": "VWNsb3VkQDEyMw==",
                    "ImageId": "uimage-32hxo4",
                    "Flavor": {
                        "Id": "66689fd4-65de-4064-9f17-d8d6123da2bd",
                        "Disk": 0,
                        "RAM": 2048,
                        "Name": "快杰共享型",
                        "VCPUs": 1,
                        "CPUName": "",
                        "MaxDataDiskCount": 0,
                        "MachineType": "OM",
                        "GPUType": "",
                        "GPU": 0,
                        "CPUPlatformId": "Intel/Auto",
                        "CPUPlatformName": "Intel"
                    },
                    "BootDiskType": "CLOUD_RSSD",
                    "BootDiskSize": 20,
                    "Disks": [
                        {
                            "Type": "CLOUD_RSSD",
                            "Size": 20
                        }
                    ],
                    "VPCId": "uvnet-ivop2ysg",
                    "SubnetId": "subnet-s2q42du5",
                    "WANSGId": "firewall-oij5dter",
                    "CreateEIP": True,
                    "ChargeType": "Dynamic",
                    "OperatorName": "Bgp",
                    "EIPPayMode": "Traffic",
                    "EIPBandwidth": 1
                }
            ]
        }
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm/create',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # self.assertEqual(expect_code, r.json()['RetCode'])
        SerialNum = r.json()["Data"]["SerialNum"]
        # 把SerialNum的值存到['SerialNum']中
        globals()['SerialNum'] = SerialNum
        print(globals()['SerialNum'])

    # 获取流程状态

    def test_02_GetWorkflowInstProcess(self):
        # 将globals()['SerialNum']存的变量值赋值给SerialNum
        SerialNum = globals()['SerialNum']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetWorkflowInstProcess"
        data = {"SerialNum": SerialNum}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm/create',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        # startTime = time.time()
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()["Data"]["Nodes"] == [] or r.json()["Data"]["Nodes"][-1]["NodeCode"] != "end_node":
                continue
            elif r.json()["Data"]["Nodes"][-1]["NodeCode"] == "end_node" and \
                    r.json()["Data"]["Nodes"][-1]["NodeStatus"] == 2:
                print("创建成功并绑定到组织")
                break
            else:
                print('查询异常')
        print("--------------", r.json()["Data"]["Nodes"][-1]["NodeTitle"])
        cmpUuids = r.json()["Data"]["Nodes"][-1]["Context"]["CreateVMResponse"]["ResourceIds"]
        globals()['cmpUuids'] = cmpUuids
        print(globals()['cmpUuids'])
        # print(type(cmpUuids))
        # cmpUuid = ''.join(cmpUuids)
        # print(cmpUuid)
        # print(type(cmpUuid))
        # ResourceId = cmpUuid[9:]
        # print(ResourceId)

    # 关机
    def test_03_StopVM(self):
        cmpUuids = globals()['cmpUuids']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=StopVM"
        data = {"ResourceIds": cmpUuids}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])
        print(r.json()["Data"]["ResourceIds"])

    # 获取云主机状态（已关机）
    def test_04_GetResourceDetail(self):
        pass

    # 开机
    def test_05_StartVM(self):
        cmpUuids = globals()['cmpUuids']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=StartVM"
        data = {"ResourceIds": cmpUuids}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])
        print(r.json()["Data"]["ResourceIds"])

    # 获取云主机状态（运行中）
    def test_06_GetResourceDetail(self):
        pass

    # 重启
    def test_07_RebootVM(self):
        cmpUuids = globals()['cmpUuids']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=RebootVM"
        data = {"ResourceIds": cmpUuids}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])
        print(r.json()["Data"]["ResourceIds"])

    # 获取云主机状态（运行中）
    def test_08_GetResourceDetail(self):
        pass
    # 改配
# 重置密码
# 制作镜像
# 删除云主机
