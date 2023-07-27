##
# Copyright (2023, ) Institute of Software, Chinese Academy of Sciences
##

import time
from kubernetes import client, config
from create_pv import create_pv
from delete_pv import delete_pv

__author__ = ('AoLuo Zhang <zhangaoluo22@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

class PVCWatchHandler:
    def __init__(self,url,token):
        self.url=url
        self.token=token
        self.createPV = create_pv(url,token)

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
        #print(pvc_list)
        self.createPV.get_pvc_info(pvc_list)
        self.createPV.create_pv()

    def DoModified(self, pvc_object):
        print("PVC MODIFIED: ", pvc_object["metadata"]["name"])

    def DoDeleted(self, pvc_object):
        print("PVC DELETED: ", pvc_object["metadata"]["name"])
        #clean unbound PV
        deletePV = delete_pv(self.url,self.token)
        deletePV.delete_pv(pvc_object["metadata"]["name"])

