import time

class Transaction(object):


    def __init__(self,humidity,temperature):
        self.type = 'T'
        self.timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.humidity = self.humidity = humidity
        self.temperature = self.temperature  = temperature 


# Test code

'''
import json
if __name__=='__main__':
    tx = Transaction('150','32')
    temp = json.dumps(tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    temps = json.loads(temp)
    print (temps, type(temps), type(temp))
'''
