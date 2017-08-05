### 각 블록들의 key 값은 index 또는 블록 헤더 해쉬
### 각 블록 데이터는 json 형식으로 value로 저장
### Indexdb에는 가장 마지막 블록 index 정보(키) + 블록 정보(value) 저장

import leveldb
from file_manager import old_file_manager

Blockdb = leveldb.LevelDB('./Block')  # 미검증된 블록 검증 전 단순 저장
Indexdb = leveldb.LevelDB('./Index')  # 마지막 블록정보 관리를 위해서

def New_block(name): ## 이를 통해서 블록 생성 시 이에 대한 데이터 요청 가능

    #마지막 블록정보 관리
    Indexdb.Delete(b'Last_Block')
    name_ch=str(name).encode('utf-8')
    Indexdb.Put(b'Last_Block',name_ch)

    old_file_manager.Block_save(name)
    return True

def Make_block_file(): ## 블록생성시 이전 블록의 헤더 해쉬등의 정보를 가져오기 위해서 동작
    temp=Indexdb.Get(b'Last_Block')
    temp=temp.decode('utf-8')
    return temp

def Unconfirmed_block(name):
    # 비검증된 블록 일단 검증을 위해 db에 저장
    Blockdb.Delete(b'Unconfirm_Block')
    name_ch = str(name).encode('utf-8')
    Blockdb.Put(b'Unconfirm_Block',name_ch)
    ###검증 작업
    old_file_manager.Block_save(name)

    return True

def Request_block(name):

    ## 블록 정보 요청을 위해 블록 정보들을 저장 해놓은 블록 정보 저장용 db 구성(해야하나?)
    return True