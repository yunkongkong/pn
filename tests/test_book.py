import json
from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcell import OperationExcel
from common.public import *
import pytest

class TestBooK:
    excel=OperationExcel()
    obj=Requests()

    def result(self,r,row):
        assert r.status_code == 200
        assert self.excel.getExpect(row=row) in json.dumps(r.json(),ensure_ascii=False)

    def test_book_001(self):
        '''获取所有书籍的信息'''
        r=self.obj.get(url=self.excel.getUrl(row=1))
        self.result(r=r,row=1)


    def test_book_002(self):
        '''添加书籍'''
        r = self.obj.post(url=self.excel.getUrl(row=2),
                          json=self.excel.getJson(row=2))
        #self.result(r=r, row=1)
        writeContent(content=r.json()[0]['datas']['id'])
        assert self.excel.getExpect(row=2) in json.dumps(r.json(),ensure_ascii=False)

    def test_book_003(self):
        '''查看书籍'''
        r=self.obj.get(url=self.excel.getUrl(row=3))
        self.result(r=r,row=3)

    def test_book_004(self):
        '''编辑书籍信息'''
        r=self.obj.put(
            url=self.excel.getUrl(row=4),
            json=self.excel.getJson(row=4))
        self.result(r=r,row=4)

    def test_book_005(self):
        '''删除书籍信息'''
        r=self.obj.delete(
            url=self.excel.getUrl(row=5))
        self.result(r=r,row=5)



if __name__ == '__main__':
    pytest.main(["-v","-s","test_book.py"])