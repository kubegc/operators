##
# Copyright (2023, ) Institute of Software, Chinese Academy of Sciences
##

import kubesys.http_request as http_request

__author__ = ('AoLuo Zhang <zhangaoluo22@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

#get pvc list
class KubernetesAnalyzer:
    def __init__(self,url,token,config=None) -> None:
        self.PVCList = {}
        self.checkList = {}

        self.pvc_url = url + "/api/v1/persistentvolumeclaims"
        self.token=token
        self.config=config

    def getPVCList(self) -> None:
        pvc_list = []
        pvc_list_response = http_request.createRequest(url=self.pvc_url, token=self.token, method="GET", keep_json=False, config=self.config)[0]

        for pvc in pvc_list_response["items"]:
            pvc_name = pvc["metadata"]["name"]
            namespace = pvc["metadata"]["namespace"]
            storage_class = pvc["spec"].get("storageClassName")
            volume_name = pvc["spec"].get("volumeName")
            accessMods = pvc["spec"].get("accessModes")
            storage_request = pvc["spec"].get("resources").get("requests").get("storage")
            #print(pvc)

            # Check if PVC has a StorageClass and is not bound to a PV
            if storage_class and not volume_name:
                pvc_list.append({
                    "name": pvc_name,
                    "namespace": namespace,
                    "storage_class": storage_class,
                    "access_modes": accessMods,
                    "storage_request":storage_request
                })
        self.PVCList = pvc_list
    
    def checkPVCStatus(self) -> None:
        check_list = []
        pvc_list_response = http_request.createRequest(url=self.pvc_url, token=self.token, method="GET", keep_json=False, config=self.config)[0]
        for pvc in pvc_list_response["items"]:
            pvc_name = pvc["metadata"]["name"]
            namespace = pvc["metadata"]["namespace"]
            status = pvc["status"]
            check_list.append({
                "name": pvc_name,
                "namespace": namespace,
                "ststus": status
            })
        self.checkList=check_list
