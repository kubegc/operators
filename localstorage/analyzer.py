import kubesys.http_request as http_request

__author__ = ('AoLuo Zhang <zhangaoluo22@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')


class KubernetesAnalyzer:
    def __init__(self) -> None:
        self.PVCList = {}
    
    def getPVCList(self, url, token, config=None) -> None:
        pvc_list = []
        pvc_url = url + "/api/v1/persistentvolumeclaims"
        pvc_list_response = http_request.createRequest(url=pvc_url, token=token, method="GET", keep_json=False, config=config)[0]

        for pvc in pvc_list_response["items"]:
            pvc_name = pvc["metadata"]["name"]
            namespace = pvc["metadata"]["namespace"]
            storage_class = pvc["spec"].get("storageClassName")
            volume_name = pvc["spec"].get("volumeName")
            accessMods = pvc["spec"].get("accessModes")

            # Check if PVC has a StorageClass and is not bound to a PV
            if storage_class and not volume_name:
                pvc_list.append({
                    "name": pvc_name,
                    "namespace": namespace,
                    "storage_class": storage_class,
                    "access_modes": accessMods
                })
        self.PVCList = pvc_list


        
        
    
    
