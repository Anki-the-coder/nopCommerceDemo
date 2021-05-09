import logging
import requests



class logGen:
    @staticmethod
    def log():
        logging.basicConfig(filename=".\\logs\\auto.log",filemode="w")
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        return logger
