import logging


class CustomLogger:
    def __init__(self, log_file, logger_name=__name__):
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)  # 设置默认的日志级别为 DEBUG

        # 添加文件处理器
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)

        # 添加控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def __getattr__(self, attr):
        """
        Forward all other attribute lookups to the logger object.
        """
        return getattr(self._logger, attr)


# Example usage:
if __name__ == "__main__":
    logger = CustomLogger('example.log')
    logger.info('This is an info message')  # 这条消息会被记录到文件和控制台
    logger.debug('This is a debug message')  # 这条消息也会被记录到文件和控制台
