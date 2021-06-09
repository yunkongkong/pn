import json
import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml

obj=Requests()
objYaml=OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):
    # print(datas['data'])
    # print(type(datas['data']))

    r=obj.post(
        url=datas['url'],
        json=datas['data'])
    #print(json.dumps(r.json(),ensure_ascii=False))
    #print(type(json.dumps(r.json(),ensure_ascii=False)))
    assert  datas['expect'] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(["-s","-v","test_login.py"])