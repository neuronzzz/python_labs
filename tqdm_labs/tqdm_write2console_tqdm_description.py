from tqdm import tqdm
import time

pbar = tqdm(range(10))
for i in pbar:
    time.sleep(1)
    # 输出进度条
    pbar.set_description("正在执行第%s个循环" % i)
