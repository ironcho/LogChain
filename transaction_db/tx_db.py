## 각 트랜잭션의 key 값은 트랜잭션 hash
## 그 이외의 값들은 모두 리스트 형태로 value 로 저장
## [pubkey, value, sig] 형식


## json 형식이 value로 넣는 방법 찾아야함

import leveldb
from transaction_db import block_db

Mempooldb = leveldb.LevelDB('./Mempool')
try:
    Mempooldb.Get(b'Unconfirm_tx')
except:
    Mempooldb.Put(b'Unconfirm_tx',b'')
#lee="xasdf".encode('utf-8')## 변수 저장시 encoding 해주어야함



def New_transaction(name):
    # 검증된 신규 거래 삽입 시 그에 대한 정보 db에 업데이트


    k=name['transaction_hash']
    tx_hash = k
    k=k.encode('utf-8')
    name =str(name)
    name = name.encode('utf-8')

    ###### 추가로 해야함 ##########
    Mempooldb.Put(k, name) ## 신규 거래 정보 txhash 추출 해야함
    ###### 추가로 해야함 ##########

    new_data = Mempooldb.Get(b'Unconfirm_tx')
    new_data=new_data.decode('utf-8')
    new_data=str(new_data)

    new_data = new_data + " "+tx_hash #미승인된 거래에 대한 정보를 저장하기 위
    new_data= str(new_data).encode('utf-8')

    Mempooldb.Put(b'Unconfirm_tx',new_data)
    ## transaction 우선순위에 따른 정렬 필요
    return True


def check():##테스트용

    kk=Mempooldb.Get(b'Unconfirm_tx')
    kk=kk.decode('utf-8')
    return kk

def Make_block_first(number): ## 노드가 블록 생성을 위해 tx 요청 시
    total_list = []
    un_tx_list=Mempooldb.Get(b'Unconfirm_tx')

    un_tx_list=un_tx_list.decode('utf-8')
    un_tx_list=un_tx_list.split()
    print(un_tx_list)
    k=0
    for i in un_tx_list:

        if k >number :
            break

        i=i.encode('utf-8')

        temp=Mempooldb.Get(i) ##각 거래의 tx hash 받기
        temp= temp.decode('utf-8')

        Mempooldb.Delete(i)
        total_list.append(temp) ## 각 거래의 전체 거래 내역 취합

        k+=1
    return total_list


def Make_block_last(name): ## 블록을 전달 받았을 때
    # 신규 블록 생성 후 기존 mempool 내 거래 제거
    ###### 추가로 해야함 ##########
    block_db.New_block(name)
    #block_db.unconfirmed_block(name)

    return True

def Receive_new_block(name):

    block_db.Unconfirmed_block(name)

    ##tx_list=name.split() ## 블록 내 tx_hash 리스트 추출
    ###### 추가로 해야함 ##########
    ##for i in tx_list:
        ##Mempooldb.Delete(i)

    return True

def Request_tx(name): ## transaction 정보 요청

    name=str(name).encode('utf-8')

    temp = Mempooldb.Get(name)
    temp = temp.decode('utf-8')

    return temp