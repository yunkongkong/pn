import yaml
from common.public import filePath


class OperationYaml:
    def readYaml(self):
        with open(filePath(),'r',encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))

    def dictYaml(self,fileDir='config',fileName='book.yaml'):
        with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8')as f:
            return yaml.safe_load(f)

# if __name__ == '__main__':
#     obj=OperationYaml()
    # for item in obj.readYaml():
    #     print(item)
    # print(obj.dictYaml()['book_002'])