import sys
import Adafruit_DHT
import json
import time
from supplychain.device_manager import transaction

def get_sensor_value():
    
        humidity, temperature = Adafruit_DHT.read_retry(11,4)
        tx= transaction.Transaction(humidity,temperature)
        json_tx = json.dumps(tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        return json_tx 

# Test Code

if __name__ == '__main__':

    temp = get_sensor_value()
    print(temp, type(temp))
    

