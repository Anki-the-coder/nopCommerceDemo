import logging


class logGen:
    @staticmethod
    def log():
        logging.basicConfig(filename=".\\logs\\auto.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
