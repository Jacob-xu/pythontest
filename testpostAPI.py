# encoding: utf-8

import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):

    @ddt.data(
        ("15222222222", "1233"),
        ("15233333333", "2345")
    )
    # ddt.unpack对上面的元组数据进行展开
    @ddt.unpack
    def testPost(self, username_data, password_data):
        formdata = {
            "username": username_data,
            "password": password_data,
            "verify": '',
            "referer": 'https://m.imooc.com',
            "pwencode": '1'
        }
        # header部分的配置
        headers_data = {
            'User-Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5 Build / MRA58N) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 79.0.3945.45 Mobile Safari / 537.36',
            'Host': 'm.imooc.com'
        }

        # cookie部分的配置
        cookies_data = dict(imooc_uuid = '320b4363-74f5-4e72-9117-dcb94c0c6aae',
                            imooc_isnew_ct = '1574481766',
                            imooc_isnew = '1',
                            page = 'https://m.imooc.com')

        # post请求构造
        res =  requests.post(
            "https://m.imooc.com/passport/user/login",
            data = formdata,
            headers = headers_data,
            cookies = cookies_data
        )

        print(res.json())
        self.assertTrue(10005 == res.json()['status'] or 10014 == res.json()['status'])

if __name__ == "__main__":
    unittest.main()