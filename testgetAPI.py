# encoding: utf-8

import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):

    @ddt.data("App专项测试", "自动化", "Python")
    def testGet(self, queryword):
        # header部分的配置
        headers_data = {
            'User-Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5 Build / MRA58N) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 79.0.3945.45 Mobile Safari / 537.36',
            'Host': 'm.imooc.com',
            'Referer': 'https://m.imooc.com',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        # cookie部分的配置
        cookies_data = dict(imooc_uuid = '320b4363-74f5-4e72-9117-dcb94c0c6aae',
                            imooc_isnew_ct = '1574481766',
                            imooc_isnew = '1',
                            page = 'https://m.imooc.com')

        # get请求构造
        res =  requests.get(
            "https://m.imooc.com/search/?words="+queryword,
            headers = headers_data,
            cookies = cookies_data
        )

        self.assertTrue(u"共找到" in res.text)

if __name__ == "__main__":
    unittest.main()