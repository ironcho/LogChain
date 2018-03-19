import time
import json

"""
    Construct Demo transaction class
"""

class Transaction(object):

    def __init__(self, sensorValue, deviceInfo):  # rule tx에서는 recv addr이 불요하므로 제거
        """
        :param sensorValue
        :param deviceInfo
        """
        self.type = 'T'
        self.timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.tx_id = "T"+"-"+ self.timestamp
        self.sensorValue = sensorValue
        self.deviceInfo = deviceInfo

'''
# =====MODULE TEST=====
if __name__ == '__main__':
    sensorValue= {"Temp": 10, "Humidity":20}
    deviceInfo = {"Type" : "led","agent":"actuator","duration":"7000"}
    tx = Transaction(sensorValue,deviceInfo)
    temp = json.dumps(tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    temps = json.loads(temp)
    print (temps, type(temps), type(temp))
'''

