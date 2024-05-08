import logging
from tqdm import tqdm
import time

# 配置日志记录到文件
logging.basicConfig(filename='output.log', level=logging.INFO, format='%(message)s')

# 模拟一个发送请求的循环
for i in tqdm(range(100)):
    # 模拟发送请求
    time.sleep(1.5)

    # 假设这里是发送请求并获取响应的代码
    response = None  # 假设响应为空

    # 检查响应是否成功
    if response:
        # 请求成功时记录日志
        logging.info(f"请求 {i} 成功")
    else:
        # 请求失败时记录日志
        logging.info(f"请求 {i} 失败")
