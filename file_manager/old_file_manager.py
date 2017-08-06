## 기존 파일 저장 시스템
##

import os



block_storage_path = os.path.dirname(os.path.dirname(__file__)) + '\_BlockStorage' + '\\'


def Block_save(name,number):
    if not os.path.isdir(block_storage_path):
        os.mkdir(block_storage_path)

    f=open(block_storage_path+"block"+number+".dat",'w')
    name=str(name)
    f.write(name)
    f.close()
    return True

def Search_block(number):
    for root,dirs,files in os.walk(block_storage_path):
        print()

    search_file = "block"+number+".dat"
    if search_file in files:
        f=open(block_storage_path+search_file,'r')

        temp = f.read()

        return temp



