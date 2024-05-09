import logging
from tqdm import tqdm
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置日志记录器，输出到文件
logging.basicConfig(filename='requests.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 模拟的响应数据
mock_response_data = {
    f"https://www.example.com/page{i}": f"Example content for page {i}" for i in range(100)
}

# 请求函数（模拟）
def send_request(url):
    start_time = time.time()
    try:
        time.sleep(random.uniform(0.5, 1.5))
        response_content = mock_response_data.get(url, "Mock response content not found")
        logging.info(f"Mock request to {url} successful. Response content: {response_content}")
    except Exception as e:
        logging.error(f"Mock request to {url} failed with error: {str(e)}")
    finally:
        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Request to {url} processed in {processing_time:.2f} seconds")
        # 模拟延迟
        return url

# 要发送的请求列表
urls = [
    f"https://www.example.com/page{i}" for i in range(100)
]

# 创建进度条
progress_bar = tqdm(total=len(urls), desc="Sending requests", unit="request")

# 创建线程池
with ThreadPoolExecutor(max_workers=50) as executor:
    # 启动线程发送请求，并收集Future对象
    futures = [executor.submit(send_request, url) for url in urls]

    # 使用as_completed迭代Future对象，并更新进度条
    for future in as_completed(futures):
        future.result()
        progress_bar.update(1)

# 关闭进度条
progress_bar.close()
logging.info("All requests completed")
