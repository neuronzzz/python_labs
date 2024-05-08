from pyheat import PyHeat

# 创建PyHeat对象
heatmap = PyHeat()

# 读取Python代码文件
with open('example.py', 'r') as f:
    code = f.read()

# 生成热图
heatmap.create(code)

# 可选：设置热图的标题
heatmap.title("Code Heatmap")

# 显示热图
heatmap.show()
