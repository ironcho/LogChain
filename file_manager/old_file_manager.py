## 기존 파일 저장 시스템
##

import os
block_height = "0"


block_storage_path = os.path.dirname(os.path.dirname(__file__)) + '\_BlockStorage' + '\\'


def Block_save(name):
    if not os.path.isdir(block_storage_path):
        os.mkdir(block_storage_path)

    f=open(block_storage_path+"block"+block_height+".dat",'w')
    name=str(name)
    f.write(name)
    f.close()
    return True