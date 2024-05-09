import pandas as pd
from tqdm import tqdm
import time

# 创建示例 DataFrame
df = pd.DataFrame({'col1': range(10), 'col2': range(10, 20)})


# 定义一个模拟发送请求的函数
def send_request(row):
    # 模拟发送请求
    time.sleep(0.5)

    # 这里可以根据每一行的数据发送请求并处理响应
    # 在这个示例中，我们只是简单地返回行的和
    return row['col1'] + row['col2']


# 创建 tqdm 进度条对象
pbar = tqdm(total=len(df), desc="Processing rows")

# 遍历 DataFrame 的每一行
for index, row in df.iterrows():
    # 更新进度条的描述
    pbar.set_description(f"Processing row {index}")

    # 调用模拟发送请求的函数
    result = send_request(row)
    # 在这里你可以处理 result，例如将结果存储到新的列中
    # 这里只是打印结果
    # print(result)

    # 更新进度条
    pbar.update(1)

# 关闭进度条
pbar.close()
