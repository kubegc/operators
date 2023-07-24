import os.path
import sys
import yaml
from kubesys.client import KubernetesClient
from analyzer import KubernetesAnalyzer
from creat_pv import creat_pv
from watch_pvc import WatchPVC

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

#other class
def handle_pvc_event(jsonObj):
    if jsonObj["type"] == "ADDED":
        pvc = jsonObj["object"]
        storage_class = pvc.get("spec", {}).get("storageClassName", None)
        if not pvc.get("status", {}).get("phase", "") == "Bound" and storage_class:
            print("Unbound PVC with StorageClass:")
            print(pvc)
    elif jsonObj["type"] == "MODIFIED":
        pvc = jsonObj["object"]
        storage_class = pvc.get("spec", {}).get("storageClassName", None)
        if not pvc.get("status", {}).get("phase", "") == "Bound" and storage_class:
            print("Unbound PVC with StorageClass (Modified):")
            print(pvc)
    elif jsonObj["type"] == "DELETED":
        print("PVC Deleted")

#test_watch
def watchPVC() -> None:
    watcher = WatchPVC(url, token, handle_pvc_event)
    watcher.start_watch()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        watcher.stop_watch()
        sys.exit(0)

#main
if __name__ == '__main__':
    yaml_data = read_yaml_file(file_path)
    url = yaml_data.get('URL')
    token = yaml_data.get('Token')
    #creatPV(getPVCList())

    watchPVC()
