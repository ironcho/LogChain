import os
import socket
import json
database_path = os.path.dirname(
    os.path.dirname(__file__)) + '\_DataStorage' + '\\'
block_storage_path = os.path.dirname(
    os.path.dirname(__file__)) + '\_BlockStorage' + '\\'
voting_storage_path = os.path.dirname(
    os.path.dirname(__file__)) + '\_Voting' + '\\'
block_confirm_path = os.path.dirname(
    os.path.dirname(__file__)) + '\_BlockConfirm' + '\\'

voting_info_file = 'voting.txt'
node_info_file = 'NodeInfo.txt'
ledger_file = 'Transactions.txt'
block_file = "Block.txt"
block_confirm_file = "BlockConfrim.txt"


def get_my_ip():
    ip = socket.gethostbyname(socket.gethostname())

    return ip


def write(file_name, message):

    f = open(file_name, 'a')
    f.write(message)
    f.write('\n')
    f.close()


def read_all_line(file_name):

    f = open(file_name, 'r')
    line_list = []
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line_list.append(line)
    f.close()
    return line_list


def add_transaction(trx):
    write(database_path + ledger_file, trx)


def add_blockconfirm(trx):
    write(block_confirm_path + block_confirm_file, trx)


def add_voting(trx):
    write(voting_storage_path + voting_info_file, trx)


def add_block(block):
    write(block_storage_path + block_file, block)


def get_ip_list():
    f = open(database_path + node_info_file, 'r')
    ip_list = []
    while True:
        line = f.readline()
        line = line[:-1]
        if not line:
            break
        if line == "":
            break
        ip_list.append(line)

    return ip_list


def get_transaction_list():
    line_list = read_all_line(database_path + ledger_file)
    return line_list


def get_voting_list():
    voting_list = read_all_line(voting_storage_path + voting_info_file)
    return voting_list


def get_blockconfirm_list():
    block_confirm_list = read_all_line(block_confirm_path + block_confirm_file)
    return block_confirm_list


def get_number_of_transactions():
    return len(get_transaction_list())


def remove_all_transactions():
    f = open(database_path + ledger_file, 'w')
    f.write("")
    f.close()


def remove_all_voting():
    f = open(voting_storage_path + voting_info_file, 'w')
    f.write("")
    f.close()


def remove_all_blockconfirm():
    f = open(block_confirm_path + block_confirm_file, 'w')
    f.write("")
    f.close()


def remove_all_Block():
    f = open(block_storage_path + block_file, 'w')
    f.write("")
    f.close()


def create_new_block(file_name, block_json):
    f = open(block_storage_path + file_name, 'w')
    f.write(block_json)
    f.close()


def save_my_block(block_json):
    create_new_block('a_my_block', block_json)


def get_my_block():
    f = open(block_storage_path + 'a_my_block', 'r')
    block = f.read()
    f.close()
    return block


def get_last_file():
    import os
    for root, dirs, files in os.walk(block_storage_path):
        print
    return files[-1]


def get_last_block():

    block_list = []
    for (path, dir, files) in os.walk(block_storage_path):
        block_list = files

    j = 0

    for i in block_list:
        block_list[j] = int(i)
        j = j + 1

    print(type(block_list[2]))
    last_block_file_name = block_list[-1]
    last_block_tx_list = read_all_line(
        block_storage_path + last_block_file_name)
    last_block = "\n".join(last_block_tx_list)
    a = json.loads(last_block)
    print(a['block_height'])
    return a['block_height'], a['block_hash']


def get_block_height():
    return len(os.walk(block_storage_path).next()[2])


def add_node_info(node_info):
    path_info = database_path + '\\NodeInfo.txt'
    write(path_info, node_info)


# test Code


get_last_block()
