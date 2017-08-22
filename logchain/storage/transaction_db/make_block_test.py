# 블록 생성 시

from logchain.storage.transaction_db import tx_db


def test_make_block():
    aaaa = tx_db.Make_block_first(10)
    print(aaaa)
    tx_db.Make_block_last(aaaa)
