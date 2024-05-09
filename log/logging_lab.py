import logging


class Logger:
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)  # 使用当前模块的名称作为 logger 的名称
        self.logger.setLevel(logging.INFO)  # 设置默认的日志级别为 INFO

        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_message(self, message):
        self.logger.info(message)


# Example usage:
if __name__ == "__main__":
    logger = Logger('example.log')
    logger.log_message('This is an info message')  # 这条消息会被记录
