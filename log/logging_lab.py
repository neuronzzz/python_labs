import logging

class CustomLogger:
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

        formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}', style='{')  # 设置日志格式

        log_file = kwargs.get('log_file', None)
        log_to_file = kwargs.get('log_to_file', True)
        log_to_console = kwargs.get('log_to_console', True)

        if log_to_file and log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        if log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def __getattr__(self, attr):
        return getattr(self.logger, attr)

# 使用示例
my_logger = CustomLogger(log_file="app.log")
my_logger.debug("This is a debug message")
my_logger.info("This is an info message")
my_logger.warning("This is a warning message")
my_logger.error("This is an error message")
my_logger.critical("This is a critical message")
