import os
import datetime
# print(os.path.join())
# base_url = os.path.dirname(os.path.dirname(__file__))
# print(os.path.join(base_url,'data','login.yaml'))


def filePath(fileDir='data',fileName='login.yaml'):
    '''
    :param fileDir: 目录
    :param fileName: 文件的名称
    :return:
    '''
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

# 写入文件
def writeContent(content):
    print('写的时间：',datetime.datetime.now())
    with open(filePath(fileDir='data',fileName='bookID'),'w') as f:
        f.write(str(content))

# 读取文件
def readContent():
    print('读的时间：',datetime.datetime.now())
    with open(filePath(fileDir='data',fileName='bookID'),'r') as f:
        return f.read()





# print(filePath())
# print(filePath('config','config.yaml'))

# {
#     "author":"wuya",
#     "done":true.
#     "name":"API实战测试"
# }
