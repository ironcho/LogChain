# 신규 거래 수신시


from logchain.storage.transaction_db import tx_db


def test_insert_new_tx():
    transaction0 = {
        "transaction_hash": "0x1231235124312asdf31", "data": "tx1"}
    transaction1 = {
        "transaction_hash": "0x1231adfabfdba23512431231", "data": "tx2"}
    transaction2 = {
        "transaction_hash": "0x1231235124asdfasdf31231", "data": "tx3"}
    transaction3 = {
        "transaction_hash": "0x123123agfadgfba512431231", "data": "tx4"}
    transaction4 = {
        "transaction_hash": "0x1231235badfbgdb12431231", "data": "tx5"}
    transaction5 = {
        "transaction_hash": "0x12312351sbhjfh2431231", "data": "tx6"}
    transaction6 = {
        "transaction_hash": "0x1231235asdfgafd12431231", "data": "tx7"}
    transaction7 = {
        "transaction_hash": "0x1231235nshfnfg12431231", "data": "tx8"}
    transaction8 = {
        "transaction_hash": "0x1231235124nhgsdndgf31231", "data": "tx9"}
    transaction9 = {
        "transaction_hash": "0x1231235124sfhjfgh31231", "data": "tx10"}
    transaction10 = {
        "transaction_hash": "0x12312351afdgdafg2431231", "data": "tx11"}
    transaction11 = {
        "transaction_hash": "0x12312351afgfan2431231", "data": "tx12"}
    transaction12 = {
        "transaction_hash": "0x1231235124asdfvadbgf31231", "data": "tx13"}
    transaction13 = {
        "transaction_hash": "0x1231235nafnsf12431231", "data": "tx14"}
    transaction14 = {
        "transaction_hash": "0x1231235asdfanbagf12431231", "data": "tx15"}
    transaction15 = {
        "transaction_hash": "0x1231235adbfgba12431231", "data": "tx16"}
    transaction16 = {
        "transaction_hash": "0x1231235asdfsavb12431231", "data": "tx17"}
    transaction17 = {
        "transaction_hash": "0x12312351adbgfba2431231", "data": "tx18"}
    transaction18 = {
        "transaction_hash": "0x1231235asdfsaf12431231", "data": "tx19"}
    transaction19 = {
        "transaction_hash": "0x123123bgabadf512431231", "data": "tx20"}
    tx_db.New_transaction(transaction0)
    tx_db.New_transaction(transaction1)
    tx_db.New_transaction(transaction2)
    tx_db.New_transaction(transaction3)
    tx_db.New_transaction(transaction4)
    tx_db.New_transaction(transaction5)
    tx_db.New_transaction(transaction6)
    tx_db.New_transaction(transaction7)
    tx_db.New_transaction(transaction8)
    tx_db.New_transaction(transaction9)
    tx_db.New_transaction(transaction10)
    tx_db.New_transaction(transaction11)
    tx_db.New_transaction(transaction12)
    tx_db.New_transaction(transaction13)
    tx_db.New_transaction(transaction14)
    tx_db.New_transaction(transaction15)
    tx_db.New_transaction(transaction16)
    tx_db.New_transaction(transaction17)
    tx_db.New_transaction(transaction18)
    tx_db.New_transaction(transaction19)

    value_from_levelDB = tx_db.check()
    value_from_levelDB_converted = value_from_levelDB.split()
    print(value_from_levelDB_converted)
