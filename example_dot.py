#Python中*和**的用法

#1. 表示运算
a = 3;
b = 4*a;
c = 6**a;
print(b, c)

# 提示1：args 和kwargs都是约定名称，不是必须的
# 提示2： *args和**kwargs同时使用时，必须*args在前，*kwargs在后
#2. 表示函数形参
#表示将任意多个函数的实参放在一个元组(*args)和字典(*kwargs)中,
def fun(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)

fun(1, 2, 3, 4, A='a', B='b', C='c', D='d')
#args= (1, 2, 3, 4)
#kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

def fun(name, *args):
    print('你好:', name)
    for i in args:
        print("你的宠物有:", i)

fun("Geek", "dog", "cat")

def fun(**kwargs):
    for key, value in kwargs.items():
        print("{0} 喜欢 {1}".format(key, value))

fun(Geek="cat", cat="box")

#3. 表示函数实参
#如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，
#类似对元组和字典进行解引用
def fun(data1, data2, data3):
    print("data1:", data1)
    print("data2", data2)
    print("data3", data3)

args = ("one", 2, 3)
fun(*args)
kwargs = {"data1": "ones", "data2": 20, "data3":30}
fun(**kwargs)

def fun(data1, data2, data3, data4, data5, data6):
    print("data1:", data1)
    print("data2", data2)
    print("data3", data3)
    print("data4", data4)
    print("data5", data5)
    print("data6", data6)

kwargs = {"data4": "ones", "data5": 20, "data6":30}
fun(*args, **kwargs)




