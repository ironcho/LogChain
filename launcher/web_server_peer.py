import threading
import time
import json
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from service.transactionmanager import transaction
from communication.p2p import receiver
from communication.p2p import sender
from communication.p2p import node_mapping_table


def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()
    print("Web Server Start")

    'Peer setting'
    my_ip_address = file_controller.get_my_ip()
    nodeproperty.my_ip_address = my_ip_address
    set_peer.set_peer()
    print("my peer : " + str(nodeproperty.my_peer_num))

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    'Send to all node 10 transaction for one iteration'

    while True:
        transaction_count = 0
        # socket open

        while transaction_count < 10:
            recv_addr = "1AVsffe"
            extra = 0x01
            tx = transaction.Transaction(recv_addr, extra)
            temp = json.dumps(
                tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)

            # send_to_all은 mapping table에 있는 정보로 broadcasting
            # send_to_all_node는 file_controller로 부터 IP List 가지고 와서 broadcasting
            # 테스트 후에 안전한 방식으로 선택
            sender.send_to_all(temp)
            #sender.send_to_all_node(temps, nodeproperty.my_ip_address, nodeproperty.port)

            transaction_count += 1

        'For block mining, time sleep'
        time.sleep(100)
        # socket close


if __name__ == '__main__':
    main()
