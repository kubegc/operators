import os.path
import sys
import yaml
import time
from kubesys.client import KubernetesClient
from analyzer import KubernetesAnalyzer
from creat_pv import creat_pv
from watch_handler import PVCWatchHandler

__author__ = ('Tian Yu <yutian20@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

file_path = 'D:/k8s_python/account.yaml'
url=''
token=''

def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def getPVCList() -> list:
    analyzer = KubernetesAnalyzer(url=url, token=token)
    analyzer.getPVCList()
    return list(analyzer.PVCList)

def checkPVC() -> list:
    analyzer = KubernetesAnalyzer(url=url, token=token)
    analyzer.checkPVCStatus()
    return list(analyzer.checkList)

def creatPV(pvc_info) -> None:
    creatPV = creat_pv(url,token)
    creatPV.get_pvc_info(pvc_info)
    creatPV.create_pv()

def test_watch(client, namespce) -> None:
    watcher_handler = PVCWatchHandler(url,token)
    watcher = client.watchResource(kind="PersistentVolumeClaim", namespace=namespce,watcherhandler=watcher_handler)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("stop PVC watcher")
        watcher.stop()

#main
if __name__ == '__main__':
    yaml_data = read_yaml_file(file_path)
    url = yaml_data.get('URL')
    token = yaml_data.get('Token')
    client = KubernetesClient(url=url,token=token)
    test_watch(client=client,namespce="default")

    #creatPV(getPVCList())

    
