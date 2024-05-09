import logging

# 创建 logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建 FileHandler，并设置 mode 参数为 'w'
file_handler = logging.FileHandler('example.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将格式化器添加到处理器
file_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(file_handler)

# 输出日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')