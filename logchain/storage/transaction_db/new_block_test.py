from logchain.storage.transaction_db import tx_db


def test_new_block():
    aaaa = tx_db.Make_block_first(10)  # try 10
    tx_db.Receive_new_block(aaaa)
