import pprint

import pytest

from UcmpApi.com.Httpclient import HttpClient
from UcmpApi.tools.yamlContorl import read_yaml


class Test_Create_Uhost:

    @pytest.mark.parametrize('caseinfo', read_yaml())
    def test_CreateUhost(self, caseinfo):
        Test_Create_Uhost.httpclient = HttpClient()
        # /001
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        param_type = caseinfo['request']['param_type']
        method = caseinfo['request']['method']
        headers = caseinfo['request']['headers']
        res = Test_Create_Uhost.httpclient.send_request(
            method=method,
            url=url,
            param_type=param_type,
            data=data,
            headers=headers
        )

        pprint.pprint(res.json())
        assert res.json()['RetCode'] == 0


if __name__ == '__main__':
    pytest.main(['Createhost_test.py'], ['-vs'])
