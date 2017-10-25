import threading
import logging
from queue import Queue
import time
import json
from service.transactionmanager import transaction


class VotingTypeQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)


def receive_event(p_thrd_name, p_inq):
    count = 1
    while True:
        logging.debug("waiting for v type msg")
        dequeued = p_inq.get()

        tx = transaction.Transaction(dequeued)
        temp = json.dumps(
            tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)

        sender.send_to_all(temp)  # 노드들 연동 후 테스트 필요 2017-09-27

        logging.debug(str(dequeued))
        logging.debug(str(temp))

        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        count = count + 1
        time.sleep(queue_strategy.SAVE_TX_DEQUEUE_INTERVAL)
