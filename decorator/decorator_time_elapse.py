import time


# 定义装饰器函数
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Method '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result

    return wrapper


# 使用装饰器来记录方法执行时间
@log_execution_time
def my_function():
    # 模拟函数执行时间
    time.sleep(1)
    print("Function executed")


# 测试
my_function()
