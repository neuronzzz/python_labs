from tqdm import tqdm
import time
import sys

# 重定向标准输出到文件
sys.stdout = open('output.log', 'w')

# 模拟一个发送请求的循环
for i in tqdm(range(10), leave=False):
    # 模拟发送请求
    time.sleep(0.5)

    # 假设这里是发送请求并获取响应的代码
    response = None  # 假设响应为空

    # 检查响应是否成功
    if response:
        # 请求成功时打印消息
        print(f"请求 {i} 成功")
    else:
        # 请求失败时打印消息
        print(f"请求 {i} 失败")

# 关闭重定向的文件
sys.stdout.close()

# 恢复标准输出
sys.stdout = sys.__stdout__
