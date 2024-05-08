import timeit
import heartrate

heartrate.trace(browser=True)


# 定义要测试的函数
def my_function():
    result = 0
    for i in range(1000000):
        result += i
    return result


# 执行性能测试
execution_time = timeit.timeit(my_function, number=10)  # 测试函数执行10次的平均时间

# 打印执行时间
print(f"Average Execution Time: {execution_time} seconds")
