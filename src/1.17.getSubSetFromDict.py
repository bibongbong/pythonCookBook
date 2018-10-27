
#   从一个字典中提取一个子集
#   1. 字典推导

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

# 对字典推导时，应该用 for ... in prices.items()
# 如果用 for... in prices，会出现如下ValueError
# ValueError: too many values to unpack (expected 2)
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)   # {'AAPL': 612.78, 'IBM': 205.55}

# 这个例子是从prices中取出，key在tech_names的元素
# 有点像1.16过滤序列元素里的compress的功能，用一个相关序列来过滤某个序列
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)   # {'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}

# 把一个元组传递给dict()函数的方法和字典推导效果一样，但速度远不如字典推导
p3 = dict((key, value) for key, value in prices.items() if key in tech_names)
print(p3)