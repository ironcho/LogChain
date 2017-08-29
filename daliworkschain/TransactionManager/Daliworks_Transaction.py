import http.client
import json
import ast
from StorageManager import FileController

def Daliworks_Transaction():
    conn = http.client.HTTPSConnection("api.thingplus.net")

    headers = {
        'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI1MTg1IiwiY2xpZW50SWQiOiJibG9ja2NoYWluX3Rlc3QiLCJpYXQiOjE0ODM0Mjg0NzIsImV4cCI6MTQ4NDcyNDQ3Mn0.DnO5qQ_VctlgxH4TDDE8V58jaYlHFhrncCw4UxaeLCc",
        'cache-control': "no-cache",
        'postman-token': "df0a8233-2858-4980-418f-79a1ce86441a"
    }

    conn.request("GET", "/v1/gateways/b827eb064a2c/sensors/b827eb064a2c-0-temp/series", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data_r = ast.literal_eval(data)
    jsonString = json.dumps(data_r,indent=4, default=lambda o: o.__dict__, sort_keys=True)
    FileController.add_transaction(jsonString)

    conn.close()

# test Code
'''
from StorageManager import FileController
from MerkleTree import GetMerkleHash
Daliworks_Transaction()
list=FileController.get_transaction_list()
print (list)
Merkletreehash=GetMerkleHash.GetMerkleHash()
print(Merkletreehash)
'''