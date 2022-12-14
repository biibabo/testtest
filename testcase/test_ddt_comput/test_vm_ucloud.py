# -*- coding: UTF-8 -*-
import logging
import time
import uuid

import polling as polling
import requests
from ddt import ddt, file_data
import unittest
from BeautifulReport import BeautifulReport
from core.basecase import BaseCase


# @ddt
class TestCreatevm(BaseCase):
    # @file_data("../../testdata/test_vm/test_vm_ucloud.json")
    # 创建ucloud云主机
    def test_01_WorkflowCreateVM(self):
        Name = uuid.uuid4()
        Name = str(Name)
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
                    "Name": Name,
                    "Count": 1,
                    "RegionEn": "cn-sh2",
                    "ZoneEn": "cn-sh2-01",
                    "MachineType": "O",
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
                        "Name": "快杰O型",
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
        # cmpUuids = globals()['cmpUuids']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=StopVM"
        data = {"ResourceIds": "2.ucloud.uhost-e1a517baqhu"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])
        print(r.json()["Data"]["ResourceIds"])

    # 获取云主机状态（已关机）
    def test_04_GetResourceDetail(self):
        # cmpUuids = globals()['cmpUuids']
        # cmpUuid = ''.join(cmpUuids)
        url = 'https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail'
        data = {"cmpUuid": "2.ucloud.uhost-e1a517baqhu", "ResourceType": "vm"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()['Data']['Status'] != 4:
                continue
            elif r.json()['Data']['Status'] == 4:
                break
            else:
                print('查询异常')
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual(4, r.json()['Data']['Status'])
        self.Status = r.json()['Data']['Status']
        self.DiskcResourceId = r.json()['Data']['DiskDetails'][0]['ResourceId']
        self.DiskUsage = r.json()['Data']['DiskDetails'][0]['DiskUsage']
        print('磁盘类型：', self.DiskUsage,'DiskcResourceId：',self.DiskcResourceId)
        self.DiskcResourceId = r.json()['Data']['DiskDetails'][1]['ResourceId']
        self.DiskUsage = r.json()['Data']['DiskDetails'][1]['DiskUsage']
        print('磁盘类型：', self.DiskUsage, 'DiskcResourceId：', self.DiskcResourceId)
        print(self.Status)

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
        cmpUuids = globals()['cmpUuids']
        cmpUuid = ''.join(cmpUuids)
        url = 'https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail'
        data = {"cmpUuid": cmpUuid, "ResourceType": "vm"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()['Data']['Status'] != 2:
                continue
            elif r.json()['Data']['Status'] == 2:
                break
            else:
                print('查询异常')
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual(2, r.json()['Data']['Status'])
        print(r.json()['Data']['Status'])

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
        cmpUuids = globals()['cmpUuids']
        cmpUuid = ''.join(cmpUuids)
        url = 'https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail'
        data = {"cmpUuid": cmpUuid, "ResourceType": "vm"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()['Data']['Status'] != 2:
                continue
            elif r.json()['Data']['Status'] == 2:
                break
            else:
                print('查询异常')
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual(2, r.json()['Data']['Status'])
        print(r.json()['Data']['Status'])

    # 改配
    def test_09_ChangeVMConfig(self):
        # 4关机，2运行中
        self.test_04_GetResourceDetail()
        Status = self.Status
        if Status == 4:
            # cmpUuids = globals()['cmpUuids']
            # cmpUuid = ''.join(cmpUuids)
            url = "https://cmp-fe.ucloud.cn/api/gateway?Action=ChangeVMConfig"
            data = {"AccountId":2,
                    "Platform":"ucloud",
                    "ProjectId":"org-uzao3s",
                    "RegionEn":"cn-sh2",
                    "cmpUuid":"2.ucloud.uhost-e1a517baqhu",
                    "CPU":2,
                    "Memory":4,
                    "Disks":
                        [{"Id":self.DiskcResourceId,
                          "Type":26,
                          "Size":30,
                          "DiskUsage":"SystemDisk",
                          "Platform":"ucloud",
                          "DatastoreResourceId":""},
                         {"Id":"bsr-e16s4mirflc",
                          "Type":5,"Size":30,"DiskUsage":"DataDisk","Platform":"ucloud","DatastoreResourceId":""}],
                    "EIP":[{"Id":"eip-e16s4zk9cn3","Ip":"106.75.240.12","Bandwidth":2,"Type":"Bgp"}]}
            header = {
                'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
                'Origin': 'https://cmp-fe.ucloud.cn',
                'Cookie': self.cookie}
            r = self.request(method="post", url=url, json=data, headers=header)
            self.assertEqual(0, r.json()['RetCode'])
            print(r.json()["Data"]["UpdateDiskRes"][0]['Id'])
            print(r.json()["Data"]["UpdateDiskRes"][1]['Id'])

        elif Status == 2:
            self.test_03_StopVM()
        else:
            print("此状态暂不支持改配")





# 重置密码
# 制作镜像
# 删除云主机
# def suite():
#     # 创建一个测试套件
#     suite = unittest.TestSuite()
#     # 将测试用例加载到测试套件中
#     loader = unittest.TestLoader()  # 创建一个用例加载对象
#     suite.addTest(loader.loadTestsFromTestCase(TestCreatevm))
#     return suite
#
# if __name__ == '__main__':
#     br = BeautifulReport(suite())
#     br.report(filename='test_vm_ucloud.html', description='ucloud_vm_测试报告', log_path='.', report_dir='.',
#               theme='theme_memories')

if __name__ == '__main__':
    # 创建类加载的对象
    load = unittest.TestLoader()
    # 将测试类加载到测试套件中
    suit1 = load.loadTestsFromTestCase(TestCreatevm)
    # 指定执行类中的一个方法或者整个类
    suits = unittest.TestSuite([TestCreatevm("test_04_GetResourceDetail")])
    # suits = unittest.TestSuite([suit1])
    report = BeautifulReport(suits)
    report.report(filename='test_vm_ucloud1.html', description='ucloud_vm_测试报告', log_path='.', report_dir='.',
                  theme='theme_memories')
