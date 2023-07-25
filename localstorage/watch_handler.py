import time
from kubernetes import client, config
from creat_pv import creat_pv

class PVCWatchHandler:
    def __init__(self,url,token):
        self.url=url
        self.token=token
        self.creatPV = creat_pv(url,token)

    def DoAdded(self, pvc_object):
        pvc_list=[]
        pvc_name = pvc_object["metadata"]["name"]
        namespace = pvc_object["metadata"]["namespace"]
        storage_class = pvc_object["spec"].get("storageClassName")
        volume_name = pvc_object["spec"].get("volumeName")
        accessMods = pvc_object["spec"].get("accessModes")
        storage_request = pvc_object["spec"].get("resources").get("requests").get("storage")
        if storage_class and not volume_name:
            pvc_list.append({
                "name": pvc_name,
                "namespace": namespace,
                "storage_class": storage_class,
                "access_modes": accessMods,
                "storage_request":storage_request
            })
        print(pvc_list)

    def DoModified(self, pvc_object):
        print("PVC MODIFIED: ", pvc_object["metadata"]["name"])

    def DoDeleted(self, pvc_object):
        print("PVC DELETED: ", pvc_object["metadata"]["name"])

