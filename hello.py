hello = "hello world!"
HEY = hello.upper()
print(HEY)

name = "python"
helloSomething = F"hello {name}"  # F表达式,python3.6以上支持
print(helloSomething)

num = len(helloSomething)  # 字符串长度
print(num)

a = 0.154545154
print("{:.4f}".format(a))  # 小数点位数格式化
print("{:.2%}".format(a))  # 百分比格式化

mylist = ["test1", "test2", "test3"]
print(mylist)
print(mylist.index("test3"))  # 搜索列表中元素位置

mylist.append("new")  # 新增元素
print(mylist)

mylist.remove("new")  # 移除首个匹配的元素
print(mylist)

list_and_list = ["test0", "test1", ["t0", "t1"]]
print(list_and_list)
print(list_and_list[1])
print(list_and_list[2][1])  # 输出列表中第2个元素中的第1个元素

list_times = list_and_list * 3
print(list_times)

list_plus = list_and_list + mylist
print(list_plus)

print(len(list_times))
print(list_times)
print(list_times[0:5])
print(list_times[3:7])
print(list_times[-4:-2])

del list_times[2]  # 删除指定索引的元素
print(list_times)

list_insert = ['a', 'b', 'c', 'd', 'e']
print(list_insert)
list_insert.insert(2, 'h')  # 在指定位置插入元素
print(list_insert)

print(list_times.pop(3))  # pop移除指定元素并返回元素

print(list_insert.index('c', 0, 4))

list_insert.reverse()  # 将列表元素反向排列
print(list_insert)

list_extend = ['abc', 'def', 'ghi']
print(list_extend)
list_extend.extend(['jkl', 'lmn'])  # extend函数可以一次性添加多个元素,为节约内存空间,推荐使用extend函数实现大列表的连接操作
print(list_extend)

list_extend.extend(list_times)  # 使用extend函数直接连接另一个列表
print(list_extend)

list_copy = list_extend.copy()  # copy 复制列表
print(list_copy)

list_sort = ['c', 'e', 't', 'f', 'A', 'H']
list_sort.sort()  # 使用sort函数对元素排序
print(list_sort)

print(list_extend.count("test0"))  # count 统计元素在列表中出现的次数

myTuple = (1, 2, 3, 'abc')  # 元组可以包含不同类型元素,元素不可修改,但元组中包含的列表可以修改
print(myTuple)

num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 196, 1, 31, 64, 78, 415, 487, 81, 548, 41, 54, 54, 51, 542, 54)
print(max(num_tuple))  # 使用max函数输出元组中最大元素
print(min(num_tuple))  # 使用min函数输出元组中最小元素

mySet = set(num_tuple)  # 集合无序,其中元素为唯一,集合默认去重
print(num_tuple)
print(mySet)

add_set = {12, 54, 514, 4, 87, 123}
add_set.add("test")  # 使用add函数向集合中添加元素
print(add_set)

update_set = {'a', 'we', 'wet', 12}
update_set.update(add_set)  # 使用update函数合并集合
print(update_set)

update_set.remove("a")  # 使用remove删除指定元素,若集合中没有则报错
update_set.pop()  # 使用pop随机删除集合中元素,若集合中没有元素则报错
update_set.discard("www")  # 使用discard函数,集合中存在元素则删除,不存在则不执行且不报错
print(update_set)

print(update_set & mySet)  # 使用&交集连接多个集合
print(update_set | mySet)  # 使用|并集连接多个集合

myDict = {
    'name': 'test',
    'age': 21,
    'gender': 'man'
}
print(myDict)  # 打印字典
print(myDict.keys())  # 打印字典键,只能打印最外层键
print(myDict.values())  # 打印字典值
print(myDict.items())  # 使用items以列表形式返回所有键值对
print(myDict['name'])  # 打印字典指定键的值

myDict['skill'] = 'python'  # 使用该格式增加字典内容,也可用于修改已存在内容
print(myDict)

del myDict['skill']  # 使用del关键字删除字典内容
print(myDict)

print(myDict.get("agee", "未查询到对应键值"))  # 使用get函数获取指定键的值,若不存在该键值则默认返回none,或返回指定的默认内容

dict2 = myDict.copy()  # 使用copy函数复制字典
myDict.clear()  # 使用clear清空字典,此时不影响已完成复制的字典副本
print(myDict)
print(dict2)

fromkeysDict = myDict.fromkeys(add_set, 'testVlaue')  # 使用fromkeys函数可以快速创建字典,第一个参数为键,第二个参数为值
print(fromkeysDict)
print(fromkeysDict.pop(514))  # 使用pop函数删除字典指定键值并返回其删除的值
print(fromkeysDict.popitem())  # 使用popitem函数删除字典最后一项键值,并以元组形式返回该键值

fromkeysDict.setdefault('abc', 'ABC')  # 使用setdefault函数设置字典的默认键值,若该键已存在则忽略
print(fromkeysDict)

newDict = {
    'name': '测试',
    'age': 123,
    'gender': 'women',
    'skill': 'python'
}
myDict.update(newDict)  # 使用update函数将newDict的内容更新到myDict,不存在的键则进行新增
print(myDict)

print('name' in myDict)  # 使用in关键字检测元素/键是否存在于列表/字符串/元组/字典中
print('name' not in myDict)  # 使用not in关键字检测元素/键是否 不存在 于列表/字符串/元组/字典中

print('a' is 'b')  # 使用is关键字判断两个对象是否相同
print('a' is not 'b')  # 使用is not关键字判断两个对象是否不同

if 'name' in myDict:
    print('myDict中有name键')
elif 'age' in myDict:
    print('myDict中没有name键但有age键')
else:
    print('myDict中均无二键')

var = 123.456
print(type(var))
res_var = str(var)  # 使用str函数进行强制类型转换
print(type(res_var))  # 使用type函数查看数据类型

res_dict = bool(myDict)  # 容器类型转换布尔类型,有内容则为True,反之False
print(res_dict)
print(type(res_dict))

x = 0.0
y = 1.1
res_x = bool(x)
res_y = bool(y)
print(res_x)  # 数字类型转换布尔,0为False其他为真
print(res_y)

var1 = 'abc'
var2 = ''
res_var1 = bool(var1)  # 字符串属于容器类型
res_var2 = bool(var2)
print(res_var1)
print(res_var2)

res_var3 = list(var1)
print(res_var3)  # 字符串转列表时,每个字符为一个元素
res_tuple = list(myTuple)
print(myTuple)
print(res_tuple)  # 元组转列表时每个元素对应转为列表元素
res_dict = list(myDict)
print(res_dict)  # 字典转列表仅保留键

set1 = {1, 3, 456, 'afasgq'}
res_set1 = list(set1)
print(res_set1)  # 集合转列表是无序的,因为集合本身就是无序的

# 元组同列表强制转换一样,数字类型是非容器类型,不可转换
# 集合转换除了集合无序特点会导致转换结果也无序外,其余一致

list1 = [['name', 'test'], ['age', 123], ['skill', 'python']]
res_list1 = dict(list1)  # 列表转dict要求必须为二级列表,且子级列表中必须为2个元素,分别对应键和值
print(res_list1)

# 元组转字典同列表一样,字符串\集合\数字因不满足二级容器,无法转换

print(isinstance(res_list1, dict))  # isinstance函数用来判断一个对象是否为一个已知的类型,  对象,对象类型  匹配则返回True

print('=============================')

for i in res_list1:
    print(i)

print('=============================')

for a in res_list1.items():
    print(a)

print('=============================')

for x in range(0, 10, 2):  # range格式 起始,结束,步长
    print(x)

list_a = [12, 31, 64, 748, [54, 21, 54, 87, 78], [54, 87, 876, 46, 461, 1235]]
for a in list_a:
    if isinstance(a, list):
        for b in a:
            print(b)
    else:
        print(a)


# def开头定义函数,括号内为参数,若无return返回值,则默认返回none
def plus(h, j):
    return h + j


print(plus(10, 20))  # 调用函数并在对应位置给上参数


def default_arg(asd="未指定参数"):  # 指定默认参数,用于未传参时调用
    return asd


print(default_arg())


def test(xx, yy=100, zz=210):
    return xx + yy + zz


print(test(200, zz=300, yy=500))  # 普通参数在前,关键字参数在后,关键字参数之间位置无所谓


def test_1(q, *, w, e):
    return q + w + e


print(test_1(1, e=3, w=2))  # *后面的参数必须使用关键字传参


def test_2(t, *u):  # 匹配完指定的参数后,剩余参数将以元组的形式存储在可变参数中
    print(t)
    print(u)


test_2(100, 230, 345, 567, 78, 789, 234)


def test_3(**db_connect):  # 同可变参数,以字典形式存储
    print(db_connect)


test_3(user='username', passwd='password', host='127.0.0.1', port='3306')


def test_4(*v):
    print(v)


k = [14, 234, 56, 67, 78, 889, 9, 34, 35, 547]

test_4(*k)  # 传参时可以将传入参数加*或**拆解为元组或字典
