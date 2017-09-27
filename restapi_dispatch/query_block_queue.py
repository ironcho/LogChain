import threading
import logging
from queue import Queue
import time


class QueryQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        """
        :param p_thrd_id:
        :param p_thrd_name:
        """
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)


def receive_event(p_thrd_name, p_inq):
    count = 0
    while True:
        logging.debug("waiting for event")
        logging.debug(str(p_inq.get()))
        count = count + 1
        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        time.sleep(2)
