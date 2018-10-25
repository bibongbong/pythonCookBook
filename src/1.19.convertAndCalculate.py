

#   在数据序列上执行聚集函数，sum()/min()/max(),首先需要先转换或者过滤数据
#   在结合数据计算与转换的方法就是使用一个生成器表达式参数

nums = [1,3,4,5,2]
s = sum(num for num in nums)
s_square = sum(num*num for num in nums)
print(s)

# 这样做同样可以达到效果，但它会先创建一个额外的列表
# 但是当元素数量非常大的时候，这个巨大的只是使用一次就被丢弃的临时数据结构是巨大的浪费
s_bad = sum([num for num in nums])