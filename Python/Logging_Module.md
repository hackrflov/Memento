import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger('myLoggerName')
