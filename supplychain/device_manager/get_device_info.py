from uuid import getnode


def get_device():
    mac = getnode()
    return mac

# test Code
'''
if __name__ =='__main__':

    mac = get_device()
    print( mac) 
    
'''
