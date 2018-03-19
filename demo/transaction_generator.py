import random
import json
from demo import transaction


def transaction_generator():

    temp =  round(random.uniform(0,35),2)
    humidity = random.randint(50,100)
    latitude = round(random.uniform(28,50),4)

    sensorValue  = {"temp":temp,"humidity": str(humidity)+"%","latitude":latitude}

    deviceInfo = {"Type": "led", "agent": "actuator", "duration": "7000"}

    tx = transaction.Transaction(sensorValue, deviceInfo)
    temp = json.dumps(tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    return temp

'''
if __name__ == '__main__':
    transaction_generator()
'''