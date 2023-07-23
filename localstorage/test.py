import os.path
import yaml
from kubesys.client import KubernetesClient
from analyzer import KubernetesAnalyzer

file_path = 'D:/k8s_python/account.yaml'
url=''
token=''

def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def getPVCList() -> list:
    analyzer = KubernetesAnalyzer()
    analyzer.getPVCList(url=url, token=token)
    return list(analyzer.PVCList)

if __name__ == '__main__':
    yaml_data = read_yaml_file(file_path)
    url = yaml_data.get('URL')
    token = yaml_data.get('Token')

    #client = KubernetesClient(url=url,token=token) 
    print(getPVCList())