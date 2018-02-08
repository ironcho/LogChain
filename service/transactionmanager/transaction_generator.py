import logging


def save_sensorinfo(p_sensorinfo_json):
    logging.debug('request(save sensor info) rcvd...')
    savetx_q.put(p_sensorinfo_json)
    logging.debug(str(savetx_q))
    logging.debug(savetx_q.qsize())




