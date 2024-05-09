import logging
from tqdm import tqdm
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置日志记录器，输出到文件
logging.basicConfig(filename='requests.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# 请求函数（模拟）
def send_request(url):
    start_time = time.time()
    try:
        time.sleep(random.uniform(0.5, 1.5))
        logging.info(f"Mock request to {url} successful.")
    except Exception as e:
        logging.error(f"Mock request to {url} failed with error: {str(e)}")
    finally:
        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Request to {url} processed in {processing_time:.2f} seconds")


# 要发送的请求列表
urls = [
    f"https://www.example.com/page{i}" for i in range(80)
]

# 创建线程池
with ThreadPoolExecutor(max_workers=50) as executor:
    with tqdm(total=len(urls), unit="request", desc="Sending requests") as progress_bar:
        # 启动线程发送请求，并收集Future对象
        futures = {executor.submit(send_request, url): url for url in urls}  # 使用字典绑定URL和Future对象

        # 使用as_completed迭代Future对象，并更新进度条
        for future in as_completed(futures):
            url = futures[future]  # 获取对应的URL
            progress_bar.set_description(f"Sending request to {url}")  # 更新进度条的描述
            progress_bar.update(1)

logging.info("All requests completed")
