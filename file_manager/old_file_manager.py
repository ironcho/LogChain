## 기존 파일 저장 시스템
##

import os
global block_height

block_storage_path = os.path.dirname(os.path.dirname(__file__)) + '\_BlockStorage' + '\\'

def Block_save(name):
    block_height+=1
    f=open(block_storage_path+"block"+block_height+".dat",'w')

    f.write(name)
    f.close()
    return True