##
# Copyright (2023, ) Institute of Software, Chinese Academy of Sciences
##

from kubesys.http_request import createRequest
import json

__author__ = ('Tian Yu <yutian20@otcaix.iscas.ac.cn>',
              'Heng Wu <wuheng@iscas.ac.cn>')

class delete_pv:
    def __init__(self, url, token, config=None) -> None:
        self.url = url
        self.token = token
        self.config = config

    def delete_pv(self,pv_name) -> None:
        url = f"{self.url}/api/v1/persistentvolumes/{pv_name}"
        response, is_ok, status_code = createRequest(url, self.token, method="DELETE", config=self.config)

        if is_ok:
            print(f"PV '{pv_name}' was deleted successfully.")
        else:
            print(f"Failed to delete PV '{pv_name}'. Status code: {status_code}")
            print("Response content:", response.content)