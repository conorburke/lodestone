import logging

def create_stream_logger(name: str, level = logging.INFO, propogate: bool = False ):
    logger = logging.getLogger(name)
    logging.basicConfig(level=level)
    logger.propagate = propogate
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    return logger