from loguru import logger


class CustomLogger:
    def __init__(self, **kwargs):
        self.logger = logger
        log_file = kwargs.get('log_file', None)
        log_to_file = kwargs.get('log_to_file', True)
        log_to_console = kwargs.get('log_to_console', True)

        if log_to_file and log_file:
            self.logger.add(log_file, rotation="00:00", retention="7 days", level="DEBUG",
                            format="{time} - {name} - {level} - {message}")
        if log_to_console:
            self.logger.add(lambda msg: print(msg), level="DEBUG", format="{time} - {name} - {level} - {message}")

    def __getattr__(self, name):
        return getattr(self.logger, name)


# 使用示例
my_logger = CustomLogger(log_file="app.log")
my_logger.debug("This is a debug message")
my_logger.info("This is an info message")
my_logger.warning("This is a warning message")
my_logger.error("This is an error message")
my_logger.critical("This is a critical message")
