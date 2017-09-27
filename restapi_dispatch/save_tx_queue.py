import threading
import logging
from queue import Queue
import time
from restapi_dispatch import eventqueueplan


class SaveTxQueueThread(threading.Thread):
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
        # tx로 만들어서, send_to_all()

        logging.debug(str(dequeued))
        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        count = count + 1
        time.sleep(eventqueueplan.SAVE_TX_DEQUEUE_INTERVAL)

        # exception queue.Empty
