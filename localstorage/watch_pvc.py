from kubesys.client import KubernetesClient

class WatchPVC:
    def __init__(self, url, token, handler_function):
        self.client = KubernetesClient(url=url, token=token)
        self.handler_function = handler_function

    def start_watch(self):
        self.client.watchResource(kind="PersistentVolumeClaim", namespace="", watcherhandler=self.handler_function)

    def stop_watch(self):
        KubernetesClient.removeWatchers()
