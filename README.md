# operators
## localstorage
We want to be able to listen for changes(add modify delete) to the PVC in kubernetes , automatically allocate the required PV and specify where to store them

This project is based on client-python(https://github.com/kubesys/client-python)

### Installation
1. install the client-python
```
git clone --recursive https://github.com/kubesys/client-python.git
pip install .
#test that you can import kubesys.client successfully
from kubesys.client import KubernetesClient
```
2. install the operators
```
git clone https://github.com/kubesys/operators.git
```
3. Configure kubernetes url and token
```
#wirte an account.yaml file like this
URL:your kubernetes URL
Token:your kubenetes Token
```
4. change the path in test.py
```
#see line 17
file_path = "your account.yaml in step3"
```
5. run the test.py
```
python3 -u "your project path"
```
