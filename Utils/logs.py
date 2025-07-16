import logging


class loggings:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        
    def info(self, message):
        self.logger.info(message)
    def error(self, message):
        self.logger.error(message)
    def debug(self, message):
        self.logger.debug(message)  
        
    def warning(self, message):
        self.logger.warning(message)      
            