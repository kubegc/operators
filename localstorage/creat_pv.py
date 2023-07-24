from kubesys.http_request import createRequest
import json

__author__ = ('Tian Yu <yutian20@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

#pvc_info = [{'name': 'my-local-pvc', 'namespace': 'default', 'storage_class': 'local-storage', 'access_modes': ['ReadWriteOnce'], 'storage_request': '2Gi'}]

class creat_pv:
    def __init__(self, url, token, config=None) -> None:
        self.url = url
        self.token = token
        self.config = config
        self.pvc_info = []

    def get_pvc_info(self, pvc_info) -> None:
        self.pvc_info = pvc_info

    # path
    def create_pv(self):
        for pv in self.pvc_info:
            pv_data = {
                "apiVersion": "v1",
                "kind": "PersistentVolume",
                "metadata": {
                    "name": pv['name'],
                },
                "spec": {
                    "capacity": {
                        "storage": pv['storage_request'],
                    },
                    "accessModes": pv['access_modes'],
                    "persistentVolumeReclaimPolicy": "Retain",
                    "storageClassName": pv['storage_class'],
                    "hostPath": {
                        "path": f"/path/to/pv/{pv['namespace']}/{pv['name']}"
                    }
                }
            }
            #print(pv_data)
            pv_data_json = json.dumps(pv_data)
            response, ok, status_code = createRequest(
                f"{self.url}/api/v1/persistentvolumes",
                self.token,
                method="POST",
                body=pv_data_json,
                config=self.config
            )
            if ok and status_code == 201:
                print(f"Created PV: {pv['name']}")
            else:
                print(f"Failed to create PV: {pv['name']}")
                print(response)

