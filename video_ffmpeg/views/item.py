def list_to_generator(input_list):
    for item in input_list:
        yield item


my_list = [1, 2, 3, 4, 5]

my_list2 = [6, 7, 8, 9, 10]
# 调用生成器函数创建生成器
gen = list_to_generator(my_list)
gen2 = list_to_generator(my_list2)

# my_list.clear()

# 遍历生成器按需获取元素
for item in gen2:
    print("gen2", item)

for item in gen:
    print("gen", item)