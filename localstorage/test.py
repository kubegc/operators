import os.path
import sys
import yaml
import time
from kubesys.client import KubernetesClient
from analyzer import KubernetesAnalyzer
from create_pv import create_pv
from watch_handler import PVCWatchHandler

__author__ = ('Tian Yu <yutian20@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

file_path = 'D:/k8s_python/account.yaml'
url=''
token=''

#read yaml
def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

#static get pvc
def getPVCList() -> list:
    analyzer = KubernetesAnalyzer(url=url, token=token)
    analyzer.getPVCList()
    return list(analyzer.PVCList)

#check pvc status
def checkPVC() -> list:
    analyzer = KubernetesAnalyzer(url=url, token=token)
    analyzer.checkPVCStatus()
    return list(analyzer.checkList)

#use pvc info create pv
def createPV(pvc_info) -> None:
    createPV = create_pv(url,token)
    createPV.get_pvc_info(pvc_info)
    createPV.create_pv()

#watch pvc and create pv
def start_watch(client, namespce) -> None:
    watcher_handler = PVCWatchHandler(url,token)
    watcher = client.watchResource(kind="PersistentVolumeClaim", namespace=namespce,watcherhandler=watcher_handler)
    try:
        while True:
            #other things...
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

    start_watch(client=client,namespce="default")

    #createPV(getPVCList())

    
