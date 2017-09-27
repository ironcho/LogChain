import threading
import logging
from queue import Queue
import time
from restapi_dispatch import eventqueueplan


class QueryQueueThread(threading.Thread):
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
        logging.debug("waiting for event")
        dequeued = p_inq.get()

        # 어떤 노드에게 조회 요청을 보낸 후에, 해당 노드로부터 정보를 받은 후에 출력?
        # 또는 해당 노드에게 직접 접근해서 조회요청을 보내고, 정보를 받은 후에 출력

        logging.debug(str(dequeued))

        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        count = count + 1
        time.sleep(eventqueueplan.QUERY_DEQUEUE_INTERVAL)

        # exception queue.Empty
