
#  如果有多个字典或者映射，需要将它们从逻辑上合并为一个单一的映射
#  有两个如下字典，现在需要在两个字典中查找，先在a中找，如果找不到再在b中找

#   collections.ChainMap
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a, b)

print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a) 如果两个字典里有重复的键，第一个出现的也就是a中的‘z’对应的值会被返回

#   ChainMap 接受多个字典将他们在逻辑上变成一个字典
#   但它并不是真的合并在一起，只是ChainMap类在其内部创建了一个容纳这些字典的列表
#   并重新定义了一些常见的字典操作来遍历这个列表
print(c) #  ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(len(c))   #   3
print(list(c.keys()))   #   ['x', 'y', 'z']
print(list(c.values())) #   [1, 2, 3]

# 对字典的更新和删除，也总是影响ChainMap中列表的第一个字典
c['z'] = 10
c['w'] = 40
del c['x']
print(a)    #   {'w': 40, 'z': 10}
print(c)    #   ChainMap({'z': 10, 'w': 40}, {'y': 2, 'z': 4})

#  del c['y']  # KeyError: "Key not found in the first mapping: 'y'"



#   作为替代， update() 方法也可以将两个字典合并
